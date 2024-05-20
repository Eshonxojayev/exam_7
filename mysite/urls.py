from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cakezone.urls import *

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cakezone.urls')),
    path('', include('billing.urls')),
    path('', include('customers.urls')),
    path('', include('product.urls')),
    path('', include('chefs.urls')),
    path('', include('account.urls', namespace='account')),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
