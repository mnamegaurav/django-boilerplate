from django.urls import path, include

from settings.views import (
    SettingAPIView,
    GeneralInformationAPIView,
)


apipatterns = [
    path("settings/", SettingAPIView.as_view(), name="settings"),
    path("settings/general-information/", GeneralInformationAPIView.as_view()),
]

urlpatterns = [
    path("api/", include(apipatterns)),
]
