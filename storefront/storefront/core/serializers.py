from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer):
  
  class Meta(BaseUserCreateSerializer.Meta):
    fields=['id','username','password',
            'email','first_name','last_name']
    
    
    #for getting current user
class UserSerializer(BaseUserSerializer):
  class Meta(BaseUserSerializer.Meta):
    fields=['id','username','email','first_name','last_name']