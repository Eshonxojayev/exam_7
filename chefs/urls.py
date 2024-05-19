from django.urls import path
from .views import ChefApiView, CookerApiView, AssistantcookApiView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from .views import LandingPageView, UsersLogoutView, UsersLoginView, UserRegisterView, ContactView, ProfileView

router = DefaultRouter()
router.register('chefs', ChefApiView)
router.register('cooker', CookerApiView)
router.register('assistant', AssistantcookApiView)

urlpatterns = [
    path('chef/', ChefApiView.as_view(), name='chef'),
    path('cooker/', CookerApiView.as_view(), name='cooker'),
    path('assistantcook/', AssistantcookApiView.as_view(), name='assistantcook')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)