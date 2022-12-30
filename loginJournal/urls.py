from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name = 'login'),
    path('', views.user_signup, name = 'signup')
]