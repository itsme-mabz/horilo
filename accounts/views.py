from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest
from .serializers import *

class CookieDataCreateView(generics.CreateAPIView):
    queryset = CookieData.objects.all()
    serializer_class = CookieDataSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]  
    serializer_class = RegisterSerializer

import logging

logger = logging.getLogger(__name__)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]  

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            try:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
            except Exception as e:
                logger.error(f"Token creation failed: {e}")
                return Response({"error": "Login failed due to token issue."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [permissions.AllowAny]  

    def post(self, request: HttpRequest, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = User.objects.get(email=email)

        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        current_site = get_current_site(request)
        domain = current_site.domain
        reset_link = f"http://{domain}/reset-password-confirm/{uid}/{token}/"
        subject = "Password Reset Request"
        message = f"Hi {user.first_name},\n\nYou're receiving this email because you requested a password reset for your user account. Please click the link below to reset your password:\n\n{reset_link}\n\nIf you did not request this, please ignore this email."
        from_email = settings.DEFAULT_FROM_EMAIL

        try:
            email_message = EmailMessage(
                subject=subject,
                body=message,
                from_email=from_email,
                to=[email],
            )

            email_message.send(fail_silently=False)
            email_status = 'Email sent successfully'

        except Exception as e:
            email_status = f'Failed to send email: {str(e)}'

        return Response({"message": f"{email_status}"}, status=status.HTTP_200_OK)

class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    permission_classes = [permissions.AllowAny]  

    def post(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        token_generator = PasswordResetTokenGenerator()
        if user is not None and token_generator.check_token(user, token):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({"message": "Password has been reset."},
                            status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid token"},
                            status=status.HTTP_400_BAD_REQUEST)


class AccountSettingsView(generics.RetrieveUpdateAPIView):
    serializer_class = AccountSettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  



from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import Enable2FASerializer, Verify2FACodeSerializer
from .utils import send_verification_code, verify_code

class Enable2FAView(generics.UpdateAPIView):
    serializer_class = Enable2FASerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        send_verification_code(phone_number)
        return Response({"detail": "Verification code sent to your phone."}, status=status.HTTP_200_OK)

class Verify2FACodeView(generics.UpdateAPIView):
    serializer_class = Verify2FACodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = self.request.user.phone_number
        code = serializer.validated_data['code']
        verification_status = verify_code(phone_number, code)
        if verification_status == "approved":
            self.request.user.is_2fa_enabled = True
            self.request.user.save()
            return Response({"detail": "2FA enabled successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid verification code."}, status=status.HTTP_400_BAD_REQUEST)
