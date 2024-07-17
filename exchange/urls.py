from django.urls import path
from .views import get_exchange_rate

urlpatterns = [
    path('', get_exchange_rate, name='get_exchange_rate'),
]
