import tempfile

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from rent_a_house.rent_app.models import Offer

UserModel = get_user_model()


class OffersViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='testing@test.com', password='123testing123')

    def test_offersView_whenNoOffers_shouldReturnNoOffers(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('offers page'))

        self.assertEqual(0, response.context['offers'].count())

    def test_offersView_whenHasOffers_shouldReturnOffers(self):
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

        response = self.client.get(reverse('offers page'))

        self.assertEqual(1, response.context['offers'].count())
