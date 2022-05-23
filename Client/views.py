
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, authentication, generics, status, views
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from .models import Person
from .serializers import PesronSerializer,ChangePasswordSerializer

class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Person.objects.all()
    serializer_class = PesronSerializer



from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
factory = APIRequestFactory()
from django.contrib.auth import get_user_model, authenticate, login
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

class PersonViewSet(viewsets.ModelViewSet):
    """
    UserModel View.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = PesronSerializer
    queryset = Person.objects.all()


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)





class PersonList(APIView,):
    permission_classes = (IsAuthenticated,)
    serializer_class = PesronSerializer
    http_method_names = ['get']

    def get(self, request, format=None):
        id = request.user.id
        username = request.user.username
        print(id)
        print(username)


        try:
            user = User.objects.get(pk=id)
            person = Person.objects.get(Username=username)

        except User.DoesNotExist:
            user = None
        except Person.DoesNotExist:
            person = None

        print(user.id)

        serializer = PesronSerializer(person)
        print(serializer.data)

        return Response(serializer.data)




class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer




