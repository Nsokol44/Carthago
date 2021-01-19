from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='user-home'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='user_profile')
]
