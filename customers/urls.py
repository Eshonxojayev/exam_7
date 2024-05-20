from django.urls import path
from .views import CountryAPIView, CityAPIView, AddressAPIView, CustomersAPIView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register('customers', CustomersAPIView)
router.register('addresses', AddressAPIView)
router.register('city', CityAPIView)
router.register('country', CountryAPIView)

urlpatterns = [
    # path('', include(router.urls)),
    path('country/', CountryAPIView.as_view({'get': 'list'}), name='country'),
    path('city', CityAPIView.as_view({'get': 'list'}), name='city'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)