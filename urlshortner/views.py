from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from .models import ShortURL
from .serializers import ShortenSerializer, ShortURLSerializer
from .utils import encode_base62
from snowflake import SnowflakeGenerator
from django.shortcuts import redirect
generator = SnowflakeGenerator(1)   # I can pass machine id here

class ShortenView(APIView):
    def post(self, request):
        serializer = ShortenSerializer(data=request.data)
        if serializer.is_valid():
            original_url = serializer.validated_data['url']
            snowflake_id = next(generator)
            short_code = encode_base62(snowflake_id)
            short_url = ShortURL.objects.create(
                short_code=short_code,
                original_url=original_url
            )
            return Response({
                "short_url": f"http://localhost:8000/{short_code}"
            })
        return Response(serializer.errors, status=400)

class RedirectView(APIView):
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        return redirect(short_url.original_url)  

class ListUrlView(APIView):
    
    def get(self, *args, **kwargs):
        queryset = ShortURL.objects.all().order_by('-created_at')
        serializer = ShortURLSerializer(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)