from django.urls import path

from user.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('change-password/', UserChangePasswordView.as_view(), name='user-change-password'),
]
