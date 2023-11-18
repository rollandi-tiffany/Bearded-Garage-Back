from rest_framework import serializers
from django.contrib.auth import get_user_model, auth
#from rest_framework.authtoken.models import Token
from .models import Vehicle

UserModel = get_user_model()

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserModel
        fields = "__all__"
    def create(self, clean_data):
		user_obj = UserModel.objects.create_user(email=clean_data['email'], password=clean_data['password'])
		user_obj.username = clean_data['username']
		user_obj.save()
		return user_obj
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
         user = auth(username = clean_data["email"], password = clean_data["password"])
         if not user:
              raise ValidationError("USER NOT FOUND")
         return user
         
class UserSerializer(serializers.ModelSerializer):
     class Meta:
          model = UserModel
          fields = ("email", "username")    
          
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['year', 'make', 'model', 'services']    