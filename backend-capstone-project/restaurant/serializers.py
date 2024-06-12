from rest_framework import serializers
from .models import Menu, Booking, MenuItem
from django.contrib.auth.models import User


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem 
        fields = '__all__'

        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking 
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['url', 'username', 'email', 'groups']