import tempfile

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase, Client

from rent_a_house.rent_app.models import Offer

UserModel = get_user_model()


class ImageFormatValidatorTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='testing@test.com', password='123testing123')

    def test_imageFormatValidator_whenImageIsCorrect_shouldCreateOffer(self):
        offer = Offer(
            title='Test',
            city='Test City',
            description='testing',
            price=33.33,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            user=self.user,
        )

        offer.full_clean()
        offer.save()

        self.assertEqual(1, Offer.objects.all().count())

    def test_imageFormatValidator_whenImageIsIncorrect_shouldRaiseValidationError(self):
        offer = Offer(
            title='Test',
            city='Test City',
            description='testing',
            price=33.33,
            image=tempfile.NamedTemporaryFile(suffix=".gif").name,
            user=self.user,
        )
        try:
            offer.full_clean()
            offer.save()

        except Exception as ex:
            self.assertRaises(ValidationError)

        self.assertEqual(0, Offer.objects.all().count())
