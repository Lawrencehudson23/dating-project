from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.process_registration),
    path('process/login/', views.process_login),
    path('logout/', views.process_logout),
    path('about_us/', views.display_about_us),
    path('contact_us/', views.display_contact_us),
    path('registration/', views.display_registration),
    path('login/', views.display_login),
    path('message/', views.display_message),
    path('profile/', views.display_profile),
    path('1on1/', views.display_1on1),
    path('dislike/', views.dislike),
    path('like/', views.like),
]