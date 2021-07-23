from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rent_a_house.rent_app.urls')),
    path('auth/', include('rent_a_house.rent_a_house_auth.urls')),
    path('profiles/', include('rent_a_house.rent_a_house_profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
