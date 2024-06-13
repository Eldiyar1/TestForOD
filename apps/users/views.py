from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from apps.users.email import send_email_confirmation
from apps.users.models import User
from apps.users.serializers import RegisterSerializer, LoginSerializer, VerifySerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_email_confirmation(user.email)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        user_email = get_object_or_404(User, email=email)
        user = authenticate(request, username=user_email.username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "refresh_token": str(refresh),
                    "access_token": str(access),
                }
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Почта или пароль неверны!'})


class VerifyOTP(APIView):
    serializer_class = VerifySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp = serializer.validated_data.get("otp")

        user = User.objects.filter(otp=otp).first()

        if not user:
            return Response({"error": "Пользователь с таким кодом подтверждения не найден."},
                            status=status.HTTP_404_NOT_FOUND)

        user.is_active = True
        user.otp = None
        user.save()

        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)

        return Response(
            {
                "message": "Аккаунт успешно подтвержден.",
                "refresh_token": str(refresh),
                "access_token": str(access),
            },
            status=status.HTTP_200_OK
        )
