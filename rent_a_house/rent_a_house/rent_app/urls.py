from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from rent_a_house.rent_app.views import home_page, offers, my_offers, offer_details, my_offer_details, create_offer, \
    edit_offer, delete_offer, rate_offer, comment_offer

urlpatterns = [
    path('', home_page, name='home page'),
    path('offers/', offers, name='offers page'),
    path('my_offers/', my_offers, name='my offers page'),
    path('offer_details/<int:pk>', offer_details, name='offer details page'),
    path('my_offer_details/<int:pk>', my_offer_details, name='my offer details page'),
    path('create_offer/', create_offer, name='create offer'),
    path('edit_offer/<int:pk>', edit_offer, name='edit offer'),
    path('delete_offer/<int:pk>', delete_offer, name='delete offer'),
    path('rate/<int:pk>', rate_offer, name='rate offer'),
    path('comment/<int:pk>', comment_offer, name='comment offer'),
]
