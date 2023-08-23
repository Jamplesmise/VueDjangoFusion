# from django.contrib.auth.models import User
# from rest_framework import serializers
#
# from userservice.models import CustomUser
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password']
#
#     def create(self, validated_data):
#         user = CustomUser(
#             username=validated_data['username']
#         )
#         user.set_password(validated_data['password'])  # 使用set_password方法哈希密码
#         user.save()
#         return user
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
#
#         user = self.model(username=username, **extra_fields)
#         user.password = make_password(password)  # 使用 make_password 设置密码
#         user.save(using=self._db)
#         return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']  # 根据你的需求添加其他字段
    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])  # 使用set_password方法哈希密码
        user.save()
        return user
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)