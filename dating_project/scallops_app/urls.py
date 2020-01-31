from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.process_registration),
    path('process/login/', views.process_login),
    path('about_us/', views.display_about_us),
    path('contact_us/', views.display_contact_us),
    path('registration/', views.display_registration),
    path('login/', views.display_login),
    path('message/', views.display_message),
    path('profile/', views.display_profile),
    path('edit/profile/', views.display_edit_profile),
    path('process/profile/', views.process_profile),

]

