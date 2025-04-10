from django.urls import path,include
from .views import ShortenView, RedirectView, ListUrlView, HomeView

urlpatterns = [
    path('shorten/', ShortenView.as_view(), name='shorten-url'),
    path('<str:short_code>', RedirectView.as_view(), name='redirect-url'),
    path('list-urls/', ListUrlView.as_view())
]
