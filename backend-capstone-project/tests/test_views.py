from django.test import TestCase
from restaurant.models import MenuItem 
from restaurant.views import MenuItemsView  
from rest_framework.authtoken.models import Token
from rest_framework.serializers import Serializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_items = [
            MenuItem.objects.create(title="Pizza", price=10.99, inventory=5),
            MenuItem.objects.create(title="Burger", price=8.50, inventory=10),
        ]

   