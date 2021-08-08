import tempfile

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from rent_a_house.rent_app.models import Offer

UserModel = get_user_model()


class MyOffersViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='testing@test.com', password='123testing123')

    def test_myOffersView_whenNoUserCreatedOffers_shouldReturnNoOffers(self):
        self.client.force_login(self.user)
        test_user = UserModel.objects.create_user(email='random_user@gmail.com', password='randomtestuser123')

        offer = Offer(
            title='Test',
            city='Test City',
            description='testing',
            price=33.33,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            user=test_user,
        )

        offer.full_clean()
        offer.save()

        response = self.client.get(reverse('my offers page'))

        self.assertEqual(0, len(response.context['user_offers']))

    def test_myOffersView_whenUserHasCreatedOffers_shouldReturnOffers(self):
        self.client.force_login(self.user)

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

        response = self.client.get(reverse('my offers page'))

        self.assertEqual(1, len(response.context['user_offers']))

    def test_myOffersView_whenUserIsNotLoggedIn_shouldBeRepositionedToSignInView(self):
        self.client.get(reverse('my offers page'))

        self.assertTemplateUsed('sign_in.html')
