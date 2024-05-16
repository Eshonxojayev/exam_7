from django.urls import path
from .views import ChefApiView, CookerApiView, AssistantcookApiView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from .views import LandingPageView, UsersLogoutView, UsersLoginView, UserRegisterView, ContactView, ProfileView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Chefs API",
        description="Customer Application demo",
        default_version="v1",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='eshonxojayevabdullaziz@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

router = DefaultRouter()
router.register('chefs', ChefApiView)
router.register('cooker', CookerApiView)
router.register('assistant', AssistantcookApiView)

urlpatterns = [
    path('chef/', ChefApiView.as_view(), name='chef'),
    path('cooker/', CookerApiView.as_view(), name='cooker'),
    path('assistantcook/', AssistantcookApiView.as_view(), name='assistantcook'),
    path('docs-redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)