import tempfile

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from django.urls import reverse

from rent_a_house.rent_app.models import Offer

UserModel = get_user_model()


class CommentOfferViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='testing@test.com', password='123testing123')

    def test_commentOfferView_whenUserIsAuthenticated_shouldAddComment(self):
        offer = Offer.objects.create(
            title='Test',
            city='Test City',
            description='testing',
            price=33.33,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            user=self.user,
        )

        self.client.force_login(self.user)

        response = self.client.post(reverse('comment offer', kwargs={
            'pk': offer.id
        }), data={
            'text': 'Test Comment',
            'user_id': self.user.id,
            'offer_id': offer.id,
        })

        self.assertEqual(1, offer.comment_set.count())

    def test_commentOfferView_whenUserIsNotAuthenticated_shouldNotBeAbleToAddComment(self):
        offer = Offer.objects.create(
            title='Test',
            city='Test City',
            description='testing',
            price=33.33,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            user=self.user,
        )

        try:
            response = self.client.post(reverse('comment offer', kwargs={
                'pk': offer.id
            }), data={
                'text': 'Test Comment',
                'user_id': self.user.id,
                'offer_id': offer.id,
            })

        except Exception as ex:
            self.assertRaises(ValidationError)

        self.assertEqual(0, offer.comment_set.count())
