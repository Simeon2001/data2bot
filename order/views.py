from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from order.models import OrderHistory
from order.serializers import OrderSerial


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
