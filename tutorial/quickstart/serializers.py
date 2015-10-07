
from rest_framework import serializers
from .models import UserCustom


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
     )
    class Meta:
        model = UserCustom
