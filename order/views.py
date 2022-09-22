from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from order.models import OrderHistory
from order.serializers import OrderSerial
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method="post", request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'account_name': openapi.Schema(type=openapi.TYPE_STRING, description="account_number"),
        'deposit': openapi.Schema(type=openapi.TYPE_NUMBER, description="deposit"),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description="password"),
    }),
)
@api_view()
@permission_classes([IsAuthenticated])
def all_order (request):
    customer = request.user
    placed, created = OrderHistory.objects.get_or_create(customer=customer, complete=True)
    item = placed.orderitem_set.all()
    orderItems = placed.get_order_items
    orderTotal = placed.get_order_total
    context = {'orderItems':orderItems}
    serializer_class = OrderSerial(item,many=True)
    return Response(serializer_class.data)
