from django.contrib import admin
from .models import ShortURL

@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'original_url', 'created_at')
    search_fields = ('short_code', 'original_url')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
