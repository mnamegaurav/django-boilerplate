from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Django Boilerplate API",
        default_version="v1",
        description="Django Boilerplate  API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@django_boilerplate.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
)
