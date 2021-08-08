from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from rent_a_house.rent_app.models import Offer

UserModel = get_user_model()


class ProfileViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='testing@test.com', password='123testing123')

    def test_getProfileView_whenUserHasNoOffers_shouldGetDetailsWithoutOffersCount(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile page'))

        self.assertEqual(0, response.context['my_offers_count'])
        self.assertEqual(self.user.id, response.context['user'].id)

    def test_getProfileView_whenUserHasOffers_shouldGetDetailsWithOffers(self):
        self.client.force_login(self.user)

        Offer.objects.create(
            title='Test Offer',
            city='Test City',
            description='Test Description',
            price=33.33,
            available=False,
            image='path/to/image.jpg',
            user=self.user
        )

        response = self.client.get(reverse('profile page'))

        self.assertEqual(1, response.context['my_offers_count'])
        self.assertEqual(self.user.id, response.context['user'].id)
