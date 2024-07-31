from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest
from .serializers import RegisterSerializer, LoginSerializer, ResetPasswordSerializer, SetNewPasswordSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

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
