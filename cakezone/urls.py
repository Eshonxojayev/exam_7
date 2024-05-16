from django.urls import path, include
from cakezone import views

urlpatterns = [
    path('index/', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('index/', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]