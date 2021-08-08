import tempfile

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from rent_a_house.common.models import Comment
from rent_a_house.rent_app.models import Offer, Rate

UserModel = get_user_model()


class DeleteOfferViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='testing@test.com', password='123testing123')

    def test_deleteOfferView_whenOfferHasNoCommentsOrRates_shouldDeleteOffer(self):
        offer = Offer.objects.create(
            title='Test',
            city='Test City',
            description='testing',
            price=33.33,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            user=self.user,
        )

        self.assertEqual(1, Offer.objects.all().count())

        self.client.force_login(self.user)

        self.client.post(reverse('delete offer', kwargs={
            'pk': offer.id,
        }))

        self.assertEqual(0, Offer.objects.all().count())

    def test_deleteOfferView_whenOfferHasComments_shouldDeleteCommentsAndOffer(self):
        offer = Offer.objects.create(
            title='Test',
            city='Test City',
            description='testing',
            price=33.33,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            user=self.user,
        )

        Comment.objects.create(
            text='Test comment',
            user_id=self.user.id,
            offer_id=offer.id
        )

        self.assertEqual(1, offer.comment_set.count())
        self.assertEqual(1, Comment.objects.all().count())

        self.client.force_login(self.user)

        self.client.post(reverse('delete offer', kwargs={
            'pk': offer.id,
        }))

        self.assertEqual(0, Offer.objects.all().count())
        self.assertEqual(0, offer.comment_set.count())
        self.assertEqual(0, Comment.objects.all().count())

    def test_deleteOfferView_whenOfferHasRate_shouldDeleteRateAndOffer(self):
        offer = Offer.objects.create(
            title='Test',
            city='Test City',
            description='testing',
            price=33.33,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            user=self.user,
        )

        Rate.objects.create(
            user_id=self.user.id,
            offer_id=offer.id
        )

        self.assertEqual(1, offer.rate_set.count())
        self.assertEqual(1, Rate.objects.all().count())

        self.client.force_login(self.user)

        self.client.post(reverse('delete offer', kwargs={
            'pk': offer.id,
        }))

        self.assertEqual(0, Offer.objects.all().count())
        self.assertEqual(0, offer.rate_set.count())
        self.assertEqual(0, Rate.objects.all().count())
