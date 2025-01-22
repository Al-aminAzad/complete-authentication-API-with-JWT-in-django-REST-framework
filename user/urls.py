from django.urls import path

from user.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, \
    SendResetPasswordEmailView, UserPasswordResetView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('change-password/', UserChangePasswordView.as_view(), name='user-change-password'),
    path('reset-password-email/', SendResetPasswordEmailView.as_view(), name='user-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='user-reset-password'),
]
