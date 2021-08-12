import tempfile

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client, RequestFactory

from rent_a_house.rent_a_house_auth.models import RentAHouseUser
from rent_a_house.rent_app.models import Offer, Rate
from rent_a_house.rent_app.views import create_offer


class ModelTests(TestCase):
    def create_offer(self):
        self.user = RentAHouseUser.objects.create_user(email='testing@test.com', password='123testing123')
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

        return offer

    def test_create_offer_with_correct_credentials_expect_to_work_correctly(self):
        offer = self.create_offer()
        self.assertEqual(len(Offer.objects.all()), 1)

    def test_create_offer_with_incorrect_credentials_expect_to_fail(self):
        self.user = RentAHouseUser.objects.create_user(email='testing@test.com', password='123testing123')

        offer = Offer(
            title='Test',
            city='Test City',
            description='testing',
            price=33.33,
            image='',
            user=self.user,
        )

        try:
            offer.full_clean()
            offer.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)

    def test_rate_offer_with_no_rating_expect_to_succeed(self):
        offer = self.create_offer()

        rate = Rate(
            offer=offer,
            user=self.user
        )

        rate.full_clean()
        rate.save()

        self.assertEqual(offer.rate_set.count(), 1)

    # def test_rate_offer_with_rating_by_the_same_user_expect_to_remove_rate(self):
    #     offer = self.create_offer()
    #
    #     rate = Rate(
    #         offer=offer,
    #         user=self.user
    #     )
    #
    #     rate.full_clean()
    #     rate.save()
    #
    #     second_rate = Rate(
    #         offer=offer,
    #         user=self.user
    #     )
    #
    #     second_rate.full_clean()
    #     second_rate.save()
    #
    #     self.assertEqual(len(Rate.objects.all()), 0)


class ValidatorTests(TestCase):
    def test_create_offer_with_incorrect_image_format_expect_to_fail(self):
        self.user = RentAHouseUser.objects.create_user(email='testing@test.com', password='123testing123')

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
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)


class CreateOfferViewTests(TestCase):
    def setUp(self):
        self.user = RentAHouseUser.objects.create_user(email='testing@test.com', password='123testing123')

    def test_create_offer_with_correct_credentials_expect_to_succeed(self):
        self.factory = RequestFactory()
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        request = self.factory.post('/create_offer/',
                                    {'title': 'Test',
                                     'city': 'City',
                                     'description': 'testing for sure please work',
                                     'price': 33.33,
                                     'available': True,
                                     'image': [image]})
        request.user = self.user

        response = create_offer(request)
        self.assertEqual(response.status_code, 302)


        # image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        # self.client.login(email='testing@test.com', password='123testing123')
        # response = self.client.post('/create_offer/', {'title': 'Test',
        #                                                'city': 'City',
        #                                                'description': 'testing for sure please work',
        #                                                'price': 33.33,
        #                                                'available': True,
        #                                                'image': [image]})
        #                                                # 'image': image})

        # < MultiValueDict: {'image': [ < TemporaryUploadedFile: 20210622203931
        # _IMG_0109.JPG(image / jpeg) >]} >

        # < QueryDict: {'csrfmiddlewaretoken': ['vtWHZxTMgp3DeAuMpOwdguZbAiuEst2UNQa8pSk5FDqZydFuo47BZn9czAV3dY6B'],
        #               'title': ['Test'], 'city': ['City'], 'description': ['dteadsadsad'], 'price': ['33.33'],
        #               'available': ['on']} >
        self.assertEqual(response.status_code, 302)
