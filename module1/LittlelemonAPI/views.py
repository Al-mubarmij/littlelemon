from django.shortcuts import render
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.generics import ListCreateAPIView
# Create your views here.

class MenuItemvView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer