from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from account.models import User
from django.contrib.auth import get_user_model
from account.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from account import resp
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

UserModel = get_user_model()

@swagger_auto_schema(method="post", request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description=" input your name"),
        'email': openapi.Schema(type=openapi.TYPE_NUMBER, description="input your email"),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description="input your password"),
    }), operation_description="Create an Account"
)
@api_view(["post"])
@permission_classes([AllowAny])
def create_account(request):
    if request.method == "POST":
        name = request.data.get("name")
        password = request.data.get("password")
        email = request.data.get("email")
        if UserModel.objects.filter(email=email).first():
            return resp.bad("email address already taken by another user")

        else:
            data = {
                "name": name,
                "email": email,
                "password": password,
            }
            serializer_class = UserSerializer(data=data)
            serializer_class.is_valid(raise_exception=True)
            data = serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(method="post", request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description="input your email"),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description="input your password"),
    }), operation_description="Sign in to get access token"
)       
@api_view(["post"])
@permission_classes([AllowAny])
def account_login(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            log = authenticate(email=email, password=password)
            refresh = RefreshToken.for_user(log)
            return Response(
                {
                    "status": True,
                    "accesstoken": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )
        except AttributeError:
            return resp.bad("Please enter the correct email address and password")

        
        
@swagger_auto_schema(method="post", request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description="input your name"),
        'email': openapi.Schema(type=openapi.TYPE_NUMBER, description="input your email"),
    }), operation_description="To update your name or email address"
)        
@api_view(["post"])
@permission_classes([IsAuthenticated])
def update_userinfo(request):
    current_user = request.user
    print(current_user)
    if request.method == "POST":
        email = request.data.get("email")
        name = request.data.get("name")
        if email == None:
            update_name = UserModel.objects.get(email=current_user)
            update_name.name = name
            update_name.save()
            return resp.created("your name have been updated")
            print(update_name)
            print("lol")
        elif name == None:
            update_email = UserModel.objects.get(email=current_user)
            update_email.email = name
            update_email.save()
            return resp.created("your email have been updated")

        elif name != None and email != None:
            update = UserModel.objects.get(email=current_user)
            update.email = email
            update.name = name
            update.save()
            return resp.created("both email and name have been updated")





