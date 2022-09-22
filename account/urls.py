from django.urls import path
from . import views

urlpatterns = [
    path("login", views.authr_token),
    path("register", views.usercreateview),
    path("update_user", views.update_userinfo),
]
