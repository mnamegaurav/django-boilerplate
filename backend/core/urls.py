from django.urls import path, include


apipatterns = []

urlpatterns = [
    path("api/core/", include(apipatterns)),
]
