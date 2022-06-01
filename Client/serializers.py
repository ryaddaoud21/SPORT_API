from django.http import JsonResponse
from requests import Response
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from yaml import serializer

from .models import Person



class PesronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('Name', 'Username','Age','Sport', 'Email','Gender', 'Train','Weight','Height', 'Hours','Effort','Goal_Type' , 'Goal_Weight' , 'Password','Image')

from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"


from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class PesronSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = Person
        fields = ['id','Name', 'Username', 'Age', 'Sport', 'Email', 'Gender', 'Train', 'Weight', 'Height', 'Hours', 'Effort',
                  'Goal_Type', 'Goal_Weight', 'Calculate_BMR', 'Calculate_TDEE', 'Password', 'password2', 'Image','In_body']


        extra_kwargs = {
            'Name': {'required': True},
            'Username': {'required': True},
            'Password': {'required': True, 'write_only': True, 'validators': [validate_password]},
            'password2': {'required': True},
        }

    def validate(self, attrs):
        if attrs['Password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['Username'],
            email=validated_data['Email'],
            first_name=validated_data['Name'],

        )
        person = Person.objects.create(
            Name=validated_data['Name'],
            Username=validated_data['Username'],
            Age=validated_data['Age'],
            Email=validated_data['Email'],
            Password=validated_data['Password'],
            Gender=validated_data['Gender'],
            Sport=validated_data['Sport'],
            Train=validated_data['Train'],
            Weight=validated_data['Weight'],
            Height=validated_data['Height'],
            Hours=validated_data['Hours'],
            Effort=validated_data['Effort'],
            Goal_Type=validated_data['Goal_Type'],
            Goal_Weight=validated_data['Goal_Weight'],
            Image=validated_data['Image'],
            Inbody=0,

        )
        user.set_password(validated_data['Password'])
        user.save()
        person.save()


        return person


from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"



class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class RegisterSerializer(serializers.ModelSerializer):


    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Person
        fields = ['id', 'Name', 'Username', 'Age', 'Sport', 'Email', 'Gender', 'Train', 'Weight', 'Height', 'Hours',
                  'Effort',
                  'Goal_Type', 'Goal_Weight', 'Calculate_BMR', 'Calculate_TDEE', 'Password', 'password2', 'Image',
                  'In_body']

        extra_kwargs = {
            'Name': {'required': True},
            'Username': {'required': True},
            'Password': {'required': True, 'write_only': True, 'validators': [validate_password]},
            'password2': {'required': True},
        }

    def validate(self, attrs):
        if attrs['Password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['Username'],
            email=validated_data['Email'],
            first_name=validated_data['Name'],

        )

        person = Person.objects.create(
            Name=validated_data['Name'],
            Username=validated_data['Username'],
            Age=validated_data['Age'],
            Email=validated_data['Email'],
            Password=validated_data['Password'],
            Gender=validated_data['Gender'],
            Sport=validated_data['Sport'],
            Train=validated_data['Train'],
            Weight=validated_data['Weight'],
            Height=validated_data['Height'],
            Hours=validated_data['Hours'],
            Effort=validated_data['Effort'],
            Goal_Type=validated_data['Goal_Type'],
            Goal_Weight=validated_data['Goal_Weight'],
            Image=validated_data['Image'],
            Inbody=0,

        )
        user.set_password(validated_data['Password'])
        user.save()
        person.save()

        return person
