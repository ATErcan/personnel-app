from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from .serializers import RegisterSerializer

class RegisterView(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer
  
  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    user = serializer.save()
    data = serializer.data
    token = Token.objects.get(user=user)
    data['token'] = token.key
    headers = self.get_success_headers(data)
    return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    