from django.urls import path
from order import views

urlpatterns = [
    path("order_history", views.allorder, name="orders_history"),
]