from django.urls import path

from rent_a_house.rent_a_house_profiles.views import profile, edit_profile

urlpatterns = [
    path('profile/', profile, name='profile page'),
    path('profile_edit/', edit_profile, name='edit profile'),
]