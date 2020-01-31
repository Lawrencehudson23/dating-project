from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import re
import bcrypt
<<<<<<< HEAD
from django.conf import settings
from django.core.files.storage import FileSystemStorage
=======
import random
from django.http import JsonResponse
>>>>>>> bc1f3d038998ed1af356d2be65ae9e0c3a7c16ca

# Create your views here.
def index(request):
    if "user_id" not in request.session:
        return redirect("/login/")
<<<<<<< HEAD
=======

>>>>>>> bc1f3d038998ed1af356d2be65ae9e0c3a7c16ca
    context = {
        "user" : User.objects.get(id=request.session["user_id"]),
        "all_users" : User.objects.exclude(id=request.session["user_id"]),
    }
    return render(request,'base.html', context)
def display_about_us(request):
    if "user_id" not in request.session:
        return redirect("/login/")

    context = {
        "user" : User.objects.get(id=request.session["user_id"]),
        "all_users" : User.objects.exclude(id=request.session["user_id"]),
    }
    return render(request,'about_us.html',context)
def display_contact_us(request):
    if "user_id" not in request.session:
        return redirect("/login/")

    context = {
        "user" : User.objects.get(id=request.session["user_id"]),
        "all_users" : User.objects.exclude(id=request.session["user_id"]),
    }
    return render(request,'contact_us.html',context)
def display_registration(request):

    return render(request, 'registration.html')

def process_registration(request):

    errors = User.objects.user_validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/registration/')
    else:
        password = request.POST["password"]
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=pw_hash, birthday = request.POST["birthday"], gender=request.POST["gender"], city = request.POST["city"])

        request.session['user_id'] = user.id
        request.session['user_first'] = user.first_name
        return redirect('/')


def process_login(request):
    errors = {}
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    if not EMAIL_REGEX.match(request.POST['login_email']): 
        errors["login_email"] = "Please enter an email address"

    if len(request.POST['login_password']) < 1:
        errors["login_password"] = "Please enter a password"

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/login/')
    
    user = User.objects.filter(email=request.POST['login_email'])
    if user:
        print("there is a user")
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()):
            request.session["user_id"] = logged_user.id
            request.session["user_first"] = logged_user.first_name
            return redirect('/')
        else:
            messages.error(request, "Incorrect password")
            return redirect("/login/")
    else:
        messages.error(request,"User does not exist")
    return redirect("/login/")
def process_logout(request):
    request.session.delete()
    return redirect('/login/')
def display_login(request):

    return render(request, 'login.html')
def display_message(request):
<<<<<<< HEAD
    return render(request, 'message.html')

=======
    if "user_id" not in request.session:
        return redirect("/login/")

    context = {
        "user" : User.objects.get(id=request.session["user_id"]),
        "all_users" : User.objects.exclude(id=request.session["user_id"]),
    }
    return render(request, 'message.html',context)
>>>>>>> bc1f3d038998ed1af356d2be65ae9e0c3a7c16ca
def display_profile(request):
    if "user_id" not in request.session:
        return redirect("/login/")

    context = {
        "user" : User.objects.get(id=request.session["user_id"]),
        "all_users" : User.objects.exclude(id=request.session["user_id"]),
    }
    return render(request, 'profile.html',context)
def display_1on1(request):
    if "user_id" not in request.session:
        return redirect("/login/")

    context = {
        "user" : User.objects.get(id=request.session["user_id"]),
        "all_users" : User.objects.exclude(id=request.session["user_id"]),
    }
    return render(request, '1on1.html',context)
def like(request):
    pass
    return redirect('/1on1/')
def dislike(request):
    pass
    return redirect('/1on1/')
    return render(request, 'profile.html')

<<<<<<< HEAD
def display_edit_profile(request):
    return render(request, 'edit_profile.html')

def process_profile(request):
    if request.method == 'POST' and request.FILES['imgfile']:
        myfile = request.FILES['imgfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
    
    quick = request.POST
    profile = Profile.objects.create(summary = quick['summary'], interests = quick['interests'], goals = quick['goals'])
    request.session['prof_id'] = profile.id
    context ={
         'uploaded_file_url' : uploaded_file_url,
         'user' : User.objects.get(id = request.session["user_id"]),
         'profile_info' : Profile.objects.get(id =  request.session['prof_id']),
    }    
    return  render (request, 'profile.html', context)
=======
def display_game(request):
    random_id = random.randint(1,44)

    try:
        Game.objects.get(id=random_id)
        question=Game.objects.get(id=random_id)
        print("used try")
    except:
        random_id = random.randint(22,44)
        question = Game.objects.get(id=random_id)
        print("used except")
    
    logged_user = User.objects.get(id=request.session["user_id"])

    context={
        "question":question,
        "logged_user":logged_user,

    }
    return render(request,'game.html', context)

def process_game(request):
    request.session["answer_id"] = request.POST["option"]

    return redirect('/game/')

>>>>>>> bc1f3d038998ed1af356d2be65ae9e0c3a7c16ca
