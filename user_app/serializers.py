from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile


class RegistrationSerializer(serializers.ModelSerializer):
    password_verify = serializers.CharField(
        write_only=True, style={
            'input-type': 'password'
        }
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password_verify'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password1 = self.validated_data['password_verify']
        if password != password1:
            raise serializers.ValidationError({'error': 'Пароли не совпадают'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Данный email уже существует'})
        account = User(username=self.validated_data['username'], email=self.validated_data['email'])
        account.set_password(password)
        account.save()
        return account


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = UserProfile
        exclude = (
            'slug',
        )
