from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name='carthago-home'),
]
