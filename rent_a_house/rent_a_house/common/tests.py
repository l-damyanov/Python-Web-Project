from django.test import TestCase

from rent_a_house.common.models import Comment
from rent_a_house.rent_app.models import Offer


class ModelTests(TestCase):
    def test_when_correct_value_given_expect_to_create(self):
        # comment = Comment(
        #     text='testing comment section',
        #     offer_id=13,
        #     user_id=19,
        # )
        #
        # comment.full_clean()
        # comment.save()
        #
        # self.assertIsNotNone(comment)
        pass
