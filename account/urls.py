from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('api/create/', views.UserCreateView.as_view(), name='create'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('token/', views.TokenCreateView.as_view(), name='token'),
]