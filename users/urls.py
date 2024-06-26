from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    UserViewSet,
    PaymentCreateAPIView,
    PaymentListAPIView,
    UserCreateAPIView,
)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("payment/create/", PaymentCreateAPIView.as_view(), name="create"),
    path("payment/", PaymentListAPIView.as_view(), name="list"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/create/", UserCreateAPIView.as_view(), name="user_create"),
] + router.urls
