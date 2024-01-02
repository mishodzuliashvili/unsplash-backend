from django.shortcuts import render
from .permissions import IsOwner
from .models import PhotoItem
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import PhotoItemSerializer    

class PhotoItemViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoItemSerializer
    queryset = PhotoItem.objects.all()
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = PhotoItem.objects.filter(user=user)
        else:
            queryset = PhotoItem.objects.none()
        return queryset