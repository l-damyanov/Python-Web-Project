import io

from PIL import Image
from django.contrib.auth import get_user_model

from django.test import TestCase, Client
from django.urls import reverse

from rent_a_house.rent_a_house_profiles.models import Profile

UserModel = get_user_model()


class EditProfileViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='testing@test.com', password='123testing123')

    def test_editProfileView_whenUserHasNoCredentials_shouldAddCredentials(self):
        self.client.force_login(self.user)

        response = self.client.post('/profiles/profile_edit/', data={
            'first_name': 'Test',
            'last_name': 'Yee',
            'phone_number': '+35948554755'
        })

        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)

        self.assertEqual('Test', profile.first_name)
        self.assertEqual('Yee', profile.last_name)
        self.assertEqual('+35948554755', profile.phone_number)

    def test_editProfileView_whenUserHasCredentials_shouldEditCredentials(self):
        profile = Profile.objects.get(pk=self.user.id)
        profile.first_name = 'Test 1'
        profile.save()

        self.client.force_login(self.user)

        response = self.client.post('/profiles/profile_edit/', data={
            'profile_image': 'path/to/image.png',
            'first_name': 'Test',
            'last_name': 'Yee',
            'phone_number': '+35948554755',
            'user': self.user,
        })

        self.assertEqual(302, response.status_code)

        profile.refresh_from_db()

        self.assertEqual('Test', profile.first_name)
        self.assertEqual('Yee', profile.last_name)
        self.assertEqual('+35948554755', profile.phone_number)

    def test_editProfileView_whenUserHasNoImage_shouldAddImage(self):
        profile = Profile.objects.get(pk=self.user.id)

        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)

        self.client.force_login(self.user)

        response = self.client.post(reverse('edit profile'), data={
            'profile_image': file,
            'first_name': 'Test',
            'last_name': 'Yee',
            'phone_number': '+35948554755',
        })

        self.assertEqual(302, response.status_code)

        profile.refresh_from_db()

        self.assertIsNotNone(profile.profile_image)
