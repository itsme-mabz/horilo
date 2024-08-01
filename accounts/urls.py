from django.urls import path
from .views import *

urlpatterns = [
    path('store-cookies/', CookieDataCreateView.as_view(), name='store-cookies'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('reset-password/', ResetPasswordView.as_view(),
         name='reset-password'),
    path('reset-password-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
]
