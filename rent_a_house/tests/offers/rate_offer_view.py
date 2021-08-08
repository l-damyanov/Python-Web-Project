import tempfile

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from rent_a_house.rent_app.models import Offer, Rate

UserModel = get_user_model()


class RateOfferViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='testing@test.com', password='123testing123')

    def test_rateOffer_whenUserHasNotRatedIt_shouldCreateRate(self):
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

        response = self.client.post(reverse('rate offer', kwargs={
            'pk': offer.id,
        }))

        rated = Rate.objects.filter(
            user_id=self.user.id,
            offer_id=offer.id,
        )

        self.assertEqual(302, response.status_code)
        self.assertTrue(rated)

    def test_rateOffer_whenUserHasAlreadyRatedIt_shouldDeleteRate(self):
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

        Rate.objects.create(
            user_id=self.user.id,
            offer_id=offer.id
        )

        self.client.force_login(self.user)

        response = self.client.post(reverse('rate offer', kwargs={
            'pk': offer.id,
        }))

        rated = Rate.objects.filter(
            user_id=self.user.id,
            offer_id=offer.id,
        )

        self.assertFalse(rated)

        self.assertEqual(302, response.status_code)

    def test_rateOffer_whenUserHasNotRatedItButAnotherUserHas_shouldReturnCorrectRateCount(self):
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

        test_user = UserModel.objects.create_user(email='random_user@gmail.com', password='randomtestuser123')

        Rate.objects.create(
            user_id=test_user.id,
            offer_id=offer.id
        )

        self.client.force_login(self.user)
        self.assertEqual(1, offer.rate_set.count())

        response = self.client.post(reverse('rate offer', kwargs={
            'pk': offer.id,
        }))

        self.assertEqual(2, offer.rate_set.count())
