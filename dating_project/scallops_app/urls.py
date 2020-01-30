from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about_us/', views.about_us),
    path('registration/', views.registration),
    path('register', views.register),
    path('login/', views.login),
    path('process/login', views.process_login),
]