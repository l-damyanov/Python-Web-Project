import tempfile

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from django.test import TestCase, Client
from django.urls import reverse

from rent_a_house.rent_app.models import Offer

UserModel = get_user_model()


class EditOfferViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='testing@test.com', password='123testing123')

    def test_editOffer_withCorrectCredentials_shouldEditOffer(self):
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

        self.client.force_login(self.user)

        response = self.client.post(reverse('edit offer', kwargs={
            'pk': offer.id
        }), data={
            'title': 'Edited',
            'city': 'Test City',
            'description': 'testing',
            'price': 33.33,
            'image': tempfile.NamedTemporaryFile(suffix=".jpg").name,
            'user': self.user,
        })

        offer.refresh_from_db()

        self.assertEqual(302, response.status_code)
        self.assertEqual('Edited', offer.title)

    def test_editOffer_withIncorrectCredentials_shouldNotEditOffer(self):
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

        self.client.force_login(self.user)

        response = self.client.post(reverse('edit offer', kwargs={
            'pk': offer.id
        }), data={
            'title': 'testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttest',
            'city': 'Test City',
            'description': 'testing',
            'price': 33.33,
            'image': tempfile.NamedTemporaryFile(suffix=".gif").name,
            'user': self.user,
        })

        offer.refresh_from_db()

        self.assertEqual(200, response.status_code)
        self.assertRaises(ValidationError)
