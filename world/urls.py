from django.urls import path
from world import views

urlpatterns = [
    # [...]
    path('', views.Home.as_view(), name='shops-list')
]
