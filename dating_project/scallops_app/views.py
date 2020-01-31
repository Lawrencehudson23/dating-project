from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'base.html')
def display_about_us(request):
    return render(request,'about_us.html')
def display_contact_us(request):
    return render(request,'contact_us.html')
def display_registration(request):
    return render(request, 'registration.html')
def display_login(request):
    return render(request, 'login.html')
def display_message(request):
    return render(request, 'message.html')
def display_profile(request):
    return render(request, 'profile.html')
def display_1on1(request):
    return render(request, '1on1.html')