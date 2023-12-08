from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            'last_login',
            'email',
            'email_verified',
            'password',
            'is_active',
            'is_staff',
            'is_admin',
            'is_superuser',
            'groups',
            'user_permissions'
        )