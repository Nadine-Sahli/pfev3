from . import views
from django.urls import path

urlpatterns = [
path('about/', views.about, name="about"),




]