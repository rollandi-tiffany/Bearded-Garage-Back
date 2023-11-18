from rest_framework import viewsets, permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model, login, logout
from .models import Vehicle
from .serializers import UserSerializer, VehicleSerializer, UserLoginSerializer, UserSignupSerializer
from .validations import custom_validation, validate_email, validate_password

class UserSignup(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            clean_data = custom_validation(request.data)
            serializer = UserSignupSerializer(data=clean_data)

            if serializer.is_valid(raise_exception=True):
                user = serializer.create(clean_data)
                
                if user:
                    return Response(
                        data={"message": "Signup Successful", "user": serializer.data},
                        status=status.HTTP_201_CREATED
                    )

        except Exception as e:
            return Response(
                data={"message": "Signup Failed", "errors": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)      
    authentication_classes = (SessionAuthentication,)

    def post(self, req):
        data = req.data
        assert validate_email(data)
        assert validate_password(data)  
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(req, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class UserLogout(APIView):
    def post(self, req):
        logout(req)      
        return Response(status=status.HTTP_200_OK) 
    
class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)   

    def get(self, req):
        serializer = UserSerializer(req.user)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)


#class UserViewSet(viewsets.ModelViewSet):
 #   queryset = User.objects.all()
  #  serializer_class = UserSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer