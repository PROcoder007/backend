from django.db.models.base import Model
from rest_framework import serializers
from .models import Document, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'phone', 'location', 'state','encodings']
        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id','docfile']