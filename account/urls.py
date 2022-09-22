from django.urls import path
from . import views

urlpatterns = [
    path("login", views.account_login, name="login"),
    path("register", views.create_account, name="create_account"),
    path("update_user", views.update_userinfo, name="update"),
]
