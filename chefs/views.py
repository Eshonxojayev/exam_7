from django.shortcuts import render
from django.views import View
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ChefSerializer, CookerSerializer, AssistantcookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
# from customers.models import Customers
from django.contrib.auth.models import User
from rest_framework.decorators import action
from .models import Cooker, Chef, Assistantcook

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# class ChefApiView(APIView):
#     def get(self, request):
#         return Response({"message": "Hello from ChefApiView"}, status=status.HTTP_200_OK)

# class CookerApiView(APIView):
#     def get(self, request):
#         return Response({"message": "Hello from CookerApiView"}, status=status.HTTP_200_OK)

# class AssistantcookApiView(APIView):
#     def get(self, request):
#         return Response({"message": "Hello from AssistantcookApiView"}, status=status.HTTP_200_OK)



class ChefApiView(APIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def get(self, request, *args, **kwargs):
        try:
            chef = Chef.objects.get(pk=kwargs['pk'])
            serializer = ChefSerializer(chef)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        chef = Chef.objects.get(pk=kwargs['pk'])
        serializer = ChefSerializer(chef, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        chef = Chef.objects.get(pk=kwargs['pk'])
        serializer = ChefSerializer(chef, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        chef = Chef.objects.get(pk=kwargs['pk'])
        chef.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CookerApiView(APIView):
    queryset = Cooker.objects.all()
    serializer_class = CookerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    def get(self, request, *args, **kwargs):
        try:
            cooker = Cooker.objects.get(pk=self.kwargs['pk'])
            serializer = CookerSerializer(cooker)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)



    def put(self, request, *args, **kwargs):
        cooker = Cooker.objects.get(pk=request.data['pk'])
        serializer = self.serializer_class(cooker, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        cooker = Cooker.objects.get(pk=request.data['pk'])
        serializer = CookerSerializer(cooker, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        cooker = Cooker.objects.get(pk=request.data['pk'])
        serializer = self.serializer_class(cooker, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssistantcookApiView(APIView):
    queryset = Assistantcook.objects.all()
    serializer_class = AssistantcookSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def get(self, request, *args, **kwargs):
        try:
            assistantcook = Assistantcook.objects.get(pk=self.kwargs['pk'])
            serializer = AssistantcookSerializer(assistantcook)
            return Response(serializer.data)

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


        return Response(data=serializer.data, status=status.HTTP_404_NOT_FOUND)


    def put(self, request, *args, **kwargs):
        assistantcook = Assistantcook.objects.get(pk=request.data['pk'])
        serializer = self.serializer_class(assistantcook, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        assistantcook = Assistantcook.objects.get(pk=request.data['pk'])
        serializer = self.serializer_class(assistantcook, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

