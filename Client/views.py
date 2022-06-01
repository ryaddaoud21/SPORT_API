
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, authentication, generics, status, views, serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Person
from .serializers import PesronSerializer,ChangePasswordSerializer,RegisterSerializer
from rest_framework.permissions import AllowAny

class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Person.objects.all()
    serializer_class = PesronSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
factory = APIRequestFactory()
from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

class PersonViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = PesronSerializer
    queryset = Person.objects.all()





class PersonList(APIView,):

    permission_classes = (IsAuthenticated,)
    serializer_class = PesronSerializer
    http_method_names = ['get']

    '''
    @csrf_exempt
    def get(self, request, format=None):
        id = request.user.id
        username = request.user.username
        try:
            user = User.objects.get(pk=id)
            person = Person.objects.get(Username=username)

        except User.DoesNotExist:
            user = None
        except Person.DoesNotExist:
            person = None

        serializer = PesronSerializer(person)
        print(serializer.data.get(id))

        id =serializer.data['id']
        print(id)

        return JsonResponse(id,safe=False)'''




class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    model = User


    @csrf_exempt
    def get_object(self, queryset=None):
        obj = self.request.user
        print(obj)
        return obj
    @csrf_exempt
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .forms import *
from .serializers import PesronSerializer
from django.shortcuts import get_object_or_404


def login(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('Username')
            raw_password = form.cleaned_data.get('Password')
            print(username)
            print(raw_password)
            try:
                user = Person.objects.get(Username=username,Password=raw_password)
            except Person.DoesNotExist:
                user = None


            if not user:
                responseData = {
                    'Error':'this person does not exist',
                }
                return JsonResponse(responseData)
            else:
                id = user.id
                responseData = {
                    'id': id,
                }
                return JsonResponse(responseData)


    else:
        form = PersonForm()

    context = {'form': form}

    return render(request,"Client/Login.html",context)


def change_password(request):
    if request.method == 'POST':
        myform = ChangeForm(request.POST)
        if myform.is_valid() :
            data = myform.cleaned_data
            id = data['id']
            old =data['old']
            new =data['new']
            try:
                user = Person.objects.get(id=id)
                print(user)
                if not user.Password == old :
                    print('the password is incorrect')
                    responseData = {'Error': 'the password is incorrect'}
                    return JsonResponse(responseData)
                else:
                    user.Password = new
                    user.save()
                    print('the password is changed successfully')
                    responseData = {'Error': 'the password is changed successfully'}
                    return JsonResponse(responseData)
            except Person.DoesNotExist:
                user = None
                print('user does not find')
                responseData = {'Error': 'user with this id does not exist'}
                return JsonResponse(responseData)


    return render(request,"Client/ChangePassword.html")


def adds(request):
    if request.method == 'POST':
        form = Addform(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            return JsonResponse(data)
    else:
        form = Addform()
    context = {'form': form}
    return render(request,"Client/Adds.html",context)