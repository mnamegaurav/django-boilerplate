from django.contrib.auth import get_user_model

from rest_framework import serializers

from accounts.utils import create_authentication_token

User = get_user_model()


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    avatar_url = serializers.URLField()

    class Meta:
        model = User
        fields = (
            "full_name",
            "username",
            "email",
            "mobile",
            "photo",
            "is_email_verified",
            "is_mobile_verified",
            "avatar_url",
        )
        read_only_fields = (
            "is_email_verified",
            "is_mobile_verified",
            "avatar_url",
        )


class UserDeactivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("is_active",)


class JWTTokenResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def __init__(self, *args, **kwargs):
        user_id = kwargs["data"]["payload"]["user_id"]
        self.user = User.objects.get(pk=user_id)
        super().__init__(*args, **kwargs)

    def validate(self, data):
        data = super().validate(data)
        token, _ = create_authentication_token(self.user)
        data["access"] = str(token.access_token)
        data["refresh"] = str(token)
        return data
