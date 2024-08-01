from django.urls import path
from .views import *

urlpatterns = [
    path('enable-2fa/', Enable2FAView.as_view(), name='enable-2fa'),
    path('verify-2fa-code/', Verify2FACodeView.as_view(), name='verify-2fa-code'),
    path('account-settings/', AccountSettingsView.as_view(), name='account-settings'),
    path('store-cookies/', CookieDataCreateView.as_view(), name='store-cookies'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('reset-password/', ResetPasswordView.as_view(),
         name='reset-password'),
    path('reset-password-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
]