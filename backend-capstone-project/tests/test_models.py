from django.test import TestCase
from restaurant.models import MenuItem, Booking
import datetime

 
class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='IceCream', price=80, inventory=100)
        self.assertEqual(item.get_item(), 'IceCream : 80')

class BookingTest(TestCase):
    def test_booking_name(self):
        bname = Booking.objects.create(name='Khalid', no_of_guests=30, bookingDate=datetime.datetime.now())
        self.assertEqual(bname.booking_name(), 'Khalid')