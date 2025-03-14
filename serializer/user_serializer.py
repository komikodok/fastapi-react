from .base import BaseSerializer


class UserSerializer(BaseSerializer):

    class Meta:
        fields = ["id", "email", "phone_number", "hobby"]