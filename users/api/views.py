from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.db.models import Q
from users.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import UserSerializer, MyTokenObtainPairSerializer, LoginResponseSerializer
from utils.response import cached_response


class CustomPagination(PageNumberPagination):
    page_size = 10

class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            refresh = MyTokenObtainPairSerializer.get_token(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            loginresponseserializer_objects = LoginResponseSerializer(
                {
                    "user_profile": user,
                    "refresh_token": refresh_token,
                    "access_token": access_token,
                }
            )
            return cached_response(
                request=request,
                status=status.HTTP_201_CREATED,
                response_status="success",
                message="Login Successfully",
                data=loginresponseserializer_objects.data,
                meta={},
            ) 
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class SearchUserView(generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        keyword = self.request.query_params.get('search')
        if '@' in keyword:
            return User.objects.filter(email__iexact=keyword)
        return User.objects.filter(Q(username__icontains=keyword) | Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword))
