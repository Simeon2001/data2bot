from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from order.models import OrderHistory
from order.serializers import OrderSerial
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

@swagger_auto_schema(method="get", operation_description="To get your order history",)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def allorder(request):
    customer = request.user
    placed, created = OrderHistory.objects.get_or_create(customer=customer, complete=True)
    item = placed.orderitem_set.all()
    serializer_class = OrderSerial(item,many=True)
    return Response(serializer_class.data, status=status.HTTP_200_OK)
