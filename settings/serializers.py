from rest_framework import serializers

from settings.models import Setting, GeneralInformation, SocialLink


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = "__all__"


class SettingSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True)

    class Meta:
        model = Setting
        fields = "__all__"
        read_only_fields = ("social_links",)


class GeneralInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInformation
        fields = "__all__"
