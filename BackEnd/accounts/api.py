from rest_framework import viewsets
from .serializers import UsersApi

from django.contrib.auth.models import User


class UsersListApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersApi