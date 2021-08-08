import tempfile

from django.test import TestCase, Client

from django.contrib.auth import get_user_model
from django.urls import reverse

from rent_a_house.rent_a_house_profiles.models import Profile
from rent_a_house.rent_app.models import Offer

UserModel = get_user_model()


class DeleteProfileViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='testing@test.com', password='123testing123')

    def test_deleteProfile_whenProfileHasNoOffers_shouldDeleteProfile(self):
        self.client.force_login(self.user)
        Profile.objects.get(pk=self.user.id)

        self.assertEqual(1, Profile.objects.count())

        response = self.client.post(reverse('delete profile'))

        self.assertEqual(0, Profile.objects.count())

        self.assertEqual(302, response.status_code)

    def test_deleteProfile_whenProfileHasOffers_shouldDeleteProfileAndOffers(self):
        offer = Offer.objects.create(
            title='Test',
            city='Test City',
            description='testing',
            price=33.33,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            user=self.user,
        )

        self.client.force_login(self.user)

        self.assertEqual(self.user.id, offer.user_id)
        self.assertEqual(1, Offer.objects.all().count())

        response = self.client.post(reverse('delete profile'))

        self.assertEqual(0, Profile.objects.count())
        self.assertEqual(0, Offer.objects.all().count())
        self.assertEqual(302, response.status_code)
