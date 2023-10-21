from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from accounts.views import (
    UserDetailAPIView,
    UserDeactivateAPIView,
    LogOutAPIView,
)


apipatterns = [
    path("me/", UserDetailAPIView.as_view(), name="user_detail_view"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh_view"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        "me/deactivate/", UserDeactivateAPIView.as_view(), name="user_deactivate_view"
    ),
    path("me/logout/", LogOutAPIView.as_view(), name="logout_view"),
]

urlpatterns = [
    path("api/", include(apipatterns)),
]
