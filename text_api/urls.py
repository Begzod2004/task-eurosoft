from django.urls import path
from .views import DayAPIView, TextConversionAPIView

urlpatterns = [
    path('day/', DayAPIView.as_view(), name='day_profile'),
    path('text-conversion/', TextConversionAPIView.as_view(), name='text-conversion'),
]