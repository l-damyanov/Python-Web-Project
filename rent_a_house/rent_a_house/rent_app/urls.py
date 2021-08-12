from django.urls import path

from rent_a_house.rent_app.views import my_offers, my_offer_details, \
    rate_offer, comment_offer, HomePage, OffersView, offer_details, EditOfferView, delete_offer, create_offer

urlpatterns = [
    path('', HomePage.as_view(), name='home page'),
    path('offers/', OffersView.as_view(), name='offers page'),
    path('my_offers/', my_offers, name='my offers page'),
    path('offer_details/<int:pk>', offer_details, name='offer details page'),
    path('my_offer_details/<int:pk>', my_offer_details, name='my offer details page'),
    path('create_offer/', create_offer, name='create offer'),
    path('edit_offer/<int:pk>', EditOfferView.as_view(), name='edit offer'),
    path('delete_offer/<int:pk>', delete_offer, name='delete offer'),
    path('rate/<int:pk>', rate_offer, name='rate offer'),
    path('comment/<int:pk>', comment_offer, name='comment offer'),
]
