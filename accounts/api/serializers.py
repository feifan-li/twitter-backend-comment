from django.contrib.auth.models import User
from rest_framework import serializers
# 指定返回什么样的数据
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','url','username','email','password']