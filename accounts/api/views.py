from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from accounts.api.serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):#默认为支持增删查改   只读：ReadOnlyModelViewSet
    """
    API Endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]