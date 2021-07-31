from django.contrib.auth import get_user_model, login
from django.test import TestCase

from rent_a_house.rent_a_house_auth.models import RentAHouseUser


class ModelTests(TestCase):
    def test_login_with_correct_credentials_expect_lo_succeed(self):
        pass
