from django.shortcuts import render
from django.views.generic import View
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from .models import Customers
from .serializers import CustomersSerializer


class CheckOutView(View):
    def get(self, request):
        return render(request, 'checkout.html')


class TestimonialView(View):
    def get(self, request):
        return render(request, 'testimonial.html')


class CustomersView(View):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)