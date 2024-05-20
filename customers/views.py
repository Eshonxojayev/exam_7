from django.shortcuts import render, redirect
from django.views import View
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Country, City, Address, Customers
from .serializers import CountrySerializer, CitySerializer, AddressSerializer, CustomersSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CountryAPIView(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    #
    # @action(detail=True, methods=['GET'])
    # def search(self, request, *args, **kwargs):
    #     country = self.request.query_params.get('country', None)
    #     if country:
    #         queryset = Country.objects.filter(name__icontains=country)
    #         serializer = CountrySerializer(queryset, many=True)
    #         return Response(serializer.data)
    #
    # @action(detail=True, methods=['GET'])
    # def city(self, request, *args, **kwargs):
    #     city = self.request.query_params.get('city', None)
    #     if city:
    #         queryset = City.objects.filter(name__icontains=city)
    #         serializer = CitySerializer(queryset, many=True)
    #         return Response(serializer.data)
    #
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    #
    # @action(detail=True, methods=['GET'])
    # def address(self, request, *args, **kwargs):
    #     address = self.request.query_params.get('address', None)
    #     if address:
    #         queryset = Address.objects.filter(name__icontains=address)
    #         serializer = AddressSerializer(queryset, many=True)
    #         return Response(serializer.data)
    #
    #     return Response(status=status.HTTP_404_NOT_FOUND)


class CityAPIView(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    # @action(detail=True, methods=['GET'])
    # def search(self, request, *args, **kwargs):
    #     city = self.request.query_params.get('city', None)
    #     if city:
    #         queryset = City.objects.filter(name__icontains=city)
    #         serializer = CitySerializer(queryset, many=True)
    #         return Response(serializer.data)
    #
    # @action(detail=True, methods=['GET'])
    # def name(self, request, *args, **kwargs):
    #     city = self.request.query_params.get('city', None)
    #     if city:
    #         queryset = City.objects.filter(name__icontains=city)
    #         serializer = CitySerializer(queryset, many=True)
    #         return Response(serializer.data)
    #
    #     return Response*(status.HTTP_200_OK)


class AddressAPIView(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    # @action(detail=True, methods=['GET'])
    # def search(self, request, *args, **kwargs):
    #     address = self.request.query_params.get('address', None)
    #     if address:
    #         queryset = Address.objects.filter(name__icontains=address)
    #         serializer = AddressSerializer(queryset, many=True)
    #         return Response(serializer.data)
    #
    #     return (status.HTTP_200_OK)
    #
    # @action(detail=True, methods=['GET'])
    # def cart(self, request, *args, **kwargs):
    #     cart = self.request.query_params.get('cart', None)
    #     if cart:
    #         queryset = Address.objects.filter(cart__name__icontains=cart)
    #         serializer = AddressSerializer(queryset, many=True)
    #         return Response(serializer.data)
    #
    #     return (status.HTTP_200_OK)
    #
    # @action(detail=True, methods=['GET'])
    # def cart_number(self, request, *args, **kwargs):
    #     cart = self.request.query_params.get('cart', None)
    #     if cart:
    #         queryset = Address.objects.filter(cart__name__icontains=cart)
    #         serializer = AddressSerializer(queryset, many=True)
    #         return Response(serializer.data)
    #
    #     return (status.HTTP_200_OK)


class CustomersAPIView(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    @action(detail=True, methods=['GET'])
    def user_id(self, request, *args, **kwargs):
        user_id = request.user.id
        queryset = Customers.objects.filter(user_id=user_id)
        serializer = CustomersSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def create_date(self, request, *args, **kwargs):
        customer_id = request.user.id
        queryset = Customers.objects.filter(user_id=customer_id)
        serializer = CustomersSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def city(self, request, *args, **kwargs):
        city_id = request.user.id
        queryset = Customers.objects.filter(city_id=city_id)
        serializer = CustomersSerializer(queryset, many=True)
        return Response(serializer.data)

