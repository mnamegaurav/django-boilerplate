from rest_framework.mixins import RetrieveModelMixin
from rest_framework.generics import GenericAPIView

from settings.models import (
    Setting,
    GeneralInformation,
)
from settings.serializers import (
    SettingSerializer,
    GeneralInformationSerializer,
)

# Create your views here.


class SettingAPIView(RetrieveModelMixin, GenericAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

    def get_object(self):
        return Setting.get_solo()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GeneralInformationAPIView(RetrieveModelMixin, GenericAPIView):
    serializer_class = GeneralInformationSerializer
    queryset = GeneralInformation.objects.all()

    def get_object(self):
        return GeneralInformation.get_solo()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
