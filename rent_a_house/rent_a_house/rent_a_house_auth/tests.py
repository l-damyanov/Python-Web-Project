from django.contrib.auth import logout, get_user_model
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from django.urls import reverse_lazy

from rent_a_house.rent_a_house_auth.models import RentAHouseUser


class ModelTests(TestCase):
    def test_login_with_correct_credentials_expect_lo_succeed(self):
        self.user = RentAHouseUser.objects.create_user(email='testing@test.com', password='123testing123')
        self.client.login(email='testing@test.com', password='123testing123')
        self.assertEqual(RentAHouseUser.objects.exists(), True)
        self.assertNotIsInstance(self.user, AnonymousUser)


class SignInViewTests(TestCase):
    def setUp(self):
        self.user = RentAHouseUser.objects.create_user(email='testing@test.com', password='123testing123')

    def test_when_sign_in_credentials_are_correct_expect_to_succeed(self):
        response = self.client.post('/auth/sign_in/', {'email': 'testing@test.com', 'password': '123testing123'})
        self.assertEqual(response.status_code, 302)

    def test_when_sign_in_credentials_are_incorrect_expect_to_fail(self):
        response = self.client.post('/auth/sign_in/', {'email': 'testing@test.com', 'password': 'notcorrect'})
        self.assertEqual(response.status_code, 200)


class SignUpViewTests(TestCase):
    def test_when_sign_up_credentials_are_correct_expect_to_succeed(self):
        response = self.client.post('/auth/sign_up/', {'email': 'testing@test.com', 'password1': '123sdad1edsad1', 'password2': '123sdad1edsad1'})
        self.assertEqual(response.status_code, 302)

    def test_when_sign_up_credentials_are_incorrect_expect_to_fail(self):
        response = self.client.post('/auth/sign_up/', {'email': 'testing@test.com', 'password1': 'asd', 'password2': 'asd'})
        self.assertEqual(response.status_code, 200)

    def test_when_user_with_the_same_credentials_already_exists(self):
        response = self.client.post('/auth/sign_up/', {'email': 'testing@test.com', 'password1': '123sdad1edsad1',
                                                       'password2': '123sdad1edsad1'})
        self.assertEqual(response.status_code, 302)

        try:
            response = self.client.post('/auth/sign_up/', {'email': 'testing@test.com', 'password1': '123sdad1edsad1',
                                                       'password2': '123sdad1edsad1'})
        except Exception as ex:
            self.assertIsNotNone(ex)


class SignOutViewTests(TestCase):
    def setUp(self):
        self.user = RentAHouseUser.objects.create_user(email='testing@test.com', password='123testing123')

    def test_sign_out(self):
        self.assertIsNotNone(self.client)
        self.assertIsNone(self.client.logout())
