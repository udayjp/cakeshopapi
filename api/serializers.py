from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import *

class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cake
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=3)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class AddtoCartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"

class CartSerializer(serializers.ModelSerializer):
    cakeid=CakeSerializer()
    class Meta:
        model=Cart
        fields="__all__"

class AddtoOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields="__all__"

class OrdersSerializer(serializers.ModelSerializer):
    cakeid=CakeSerializer(read_only=True,many=True)
    class Meta:
        model=Orders
        fields="__all__"
