from django.test import TestCase
from rentapp.models import Rentapp


class RentappTestCase(TestCase):
    # changes data each time in test function

    def setUp(self):
        Rentapp.objects.create(location="sallaghari",owner_name="Bisesh")

    def test_owner_profile_exists(self):
        self.assertEqual()
      