from .models import PhotoItem
from rest_framework import serializers

class PhotoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoItem
        fields = ['id', 'name', 'link', 'description', 'user', 'date_created']

