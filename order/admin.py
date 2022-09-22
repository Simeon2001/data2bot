from django.contrib import admin
from order.models import OrderHistory, OrderItem, Product


admin.site.register(OrderHistory)
admin.site.register(OrderItem)
admin.site.register(Product)
