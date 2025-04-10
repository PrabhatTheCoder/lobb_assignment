from django.db import models

class ShortURL(models.Model):
    short_code = models.CharField(max_length=255, unique=True, db_index=True)
    original_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
