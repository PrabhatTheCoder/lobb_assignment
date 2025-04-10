from rest_framework import serializers
from .models import ShortURL

class ShortenSerializer(serializers.Serializer):
    url = serializers.URLField()

class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ['short_code', 'original_url', 'created_at']
