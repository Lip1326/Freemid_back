from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from user.models.user_model import UserModel


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    photo = Base64ImageField(required=False)

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'password', 'role', 'first_name', 'last_name', 'confirm_password', 'photo']

    def validate(self, data):
        # Vérifiez si les mots de passe correspondent uniquement si les deux clés sont présentes
        if 'password' in data and 'confirm_password' in data:
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError("Les mots de passe ne correspondent pas.")
        return data

    def create(self, validated_data):
        # Retirer confirm_password avant de créer l'utilisateur
        validated_data.pop('confirm_password')
        user = UserModel(**validated_data)
        user.set_password(validated_data['password'])  # Hachage du mot de passe
        user.save()
        return user
