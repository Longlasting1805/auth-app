from django.urls import path, include, re_path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django_email_verification import urls as email_urls

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name="sign_up"),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/change-password/', ChangPasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
     path('api/v1/', include(api_urlpatterns)),
    # path('email/', include(email_urls)),
    path('send_email/', sendEmail),
    # path('email/<str:token>/', confirm),
]
    