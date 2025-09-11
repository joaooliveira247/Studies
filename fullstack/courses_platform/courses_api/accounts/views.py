from django.contrib.auth.hashers import check_password, make_password
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User
from accounts.serializers import UserSerializer
from core.utils.exceptions import ValidationError
from core.utils.formatters import format_serializer_error

# Create your views here.


class SignInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request):
        email, password = (
            request.data.get("email", ""),
            request.data.get("password", ""),
        )

        if not email or not password:
            raise ValidationError

        user = User.objects.filter(email=email).first()

        if not user:
            raise AuthenticationFailed("Email não encontrado.")

        if not check_password(password, user.password):
            raise AuthenticationFailed("Senha invalida.")
        
        user_data = UserSerializer(user).data
        access_token = RefreshToken.for_user(user).access_token

        return Response(
            {
                "user": user_data,
                "access_token": str(access_token),
            }
        )


class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request):
        data = {
            "name": request.data.get("name"),
            "email": request.data.get("email"),
            "password": request.data.get("password"),
        }

        serializer = UserSerializer(data=data)

        if not serializer.is_valid():
            raise ValidationError(format_serializer_error(serializer.errors))

        user = User.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            password=make_password(data.get("password")),
        )

        access_token = RefreshToken.for_user(user).access_token

        return Response(
            {
                "user": UserSerializer(user).data,
                "access_token": str(access_token),
            }
        )
