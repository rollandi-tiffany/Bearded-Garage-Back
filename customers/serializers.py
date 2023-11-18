from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
#from rest_framework.authtoken.models import Token
from .models import Vehicle

UserModel = get_user_model()

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, validated_data):
        user_obj = UserModel.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        user_obj.username = validated_data['username']
        user_obj.save()
        return user_obj
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError("User not found")

        return data
         
class UserSerializer(serializers.ModelSerializer):
     class Meta:
          model = UserModel
          fields = ("email", "username")    

class VehicleSerializer(serializers.ModelSerializer):
     class Meta:
          model = Vehicle
          fields = ['year', 'make', 'model', 'services']    