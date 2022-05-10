from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from .models import Person
from .serializers import PesronSerializer
import json
from rest_framework.response import Response

class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Person.objects.all()
    serializer_class = PesronSerializer

    def post(self, request, pk, format=None):
        return Response("ok")




from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
factory = APIRequestFactory()
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    UserModel View.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
