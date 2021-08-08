import io

from PIL import Image
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from django.urls import reverse

from rent_a_house.rent_app.models import Offer

UserModel = get_user_model()


class CreateOfferViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='testing@test.com', password='123testing123')

    def test_createOffer_withCorrectCredentials_shouldCreateOffer(self):
        self.client.force_login(self.user)

        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)

        response = self.client.post(reverse('create offer'), {
            'title': 'Test',
            'city': 'Test City',
            'description': 'testing',
            'price': 33.33,
            'available': True,
            'image': file,
        })

        self.assertEqual(302, response.status_code)
        self.assertEqual(1, Offer.objects.all().count())

    def test_createOffer_withIncorrectCredentials_shouldNotCreateOffer(self):
        self.client.force_login(self.user)

        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'gif')
        file.name = 'test.gif'
        file.seek(0)

        response = self.client.post(reverse('create offer'), data={
            'title': 'Test',
            'city': 'Test City',
            'description': 'testing',
            'price': 33.33,
            'available': True,
            'image': file,
        })

        self.assertEqual(200, response.status_code)
        self.assertRaises(ValidationError)
