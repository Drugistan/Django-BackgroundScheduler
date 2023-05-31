from django.urls import path
from .views import CovidView

urlpatterns = [
    path('tracker/', CovidView.as_view(), name="CovidView"),
]
