from rest_framework import serializers

from .user_serializer import UserSerializer
from ..models.client_model import ClientModel
from ..models.user_model import UserModel


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(write_only=True)
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ClientModel
        fields = ['user', 'username', 'company_description', 'project_history']
        read_only_fields = ['username', 'verification_status']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserModel.objects.create(**user_data)
        client = ClientModel.objects.create(user=user, **validated_data)
        return client
