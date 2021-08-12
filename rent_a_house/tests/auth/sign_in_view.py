from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse


UserModel = get_user_model()


class SignUpViewTests(TestCase):
    def test_signUpView_withValidCredentials_shouldSignUp(self):
        response = self.client.post(reverse('sign up'), data={
            'email': 'testing@testing.testing',
            'password1': '1234testing5678',
            'password2': '1234testing5678'
        })

        self.assertEqual(302, response.status_code)

    def test_signUpView_withInvalidCredentials_shouldRaiseValidationError(self):
        try:
            response = self.client.post(reverse('sign up'), data={
                'email': 'testing@testing.testing',
                'password1': '1234',
                'password2': '1234',
            })
        except Exception as ex:
            self.assertRaises(ValidationError)
