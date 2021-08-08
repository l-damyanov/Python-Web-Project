from django.urls import path

from rent_a_house.rent_a_house_auth.views import sign_out, SignInView, SignUpView

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign up'),
    path('sign_in/', SignInView.as_view(), name='sign in'),
    path('sign_out/', sign_out, name='sign out'),
]
