from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def about_us(request):
    return render(request,'about_us.html')
def registration(request):
    return render(request, 'registration.html')
def login(request):
    return render(request, 'login.html')