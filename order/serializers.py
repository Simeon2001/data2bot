from itertools import product
from rest_framework import serializers
from order.models import OrderItem

class OrderSerial(serializers.ModelSerializer):

    product = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['id','product','quantity','total_price']
