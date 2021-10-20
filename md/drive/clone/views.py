from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User #You'll probably have to remove this when implementing sqli
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    return render(request,"clone/homepage.html")

def index(request):
    return render(request,"clone/index.html")

def signin(request):
    #for the login form 
    if request.method == 'POST':
        #Values obtained form the form 
        username = request.POST['username']
        passw = request.POST['password']

        user = authenticate(username = username,password = passw)
        if user is not None:
            login(request,user)
            return redirect('index')
        else :
            messages.error(request,passw)
            return redirect('home')
    return render(request,"clone/loginpage.html")

def signup(request):
    #for the sign up form 
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        r_password = request.POST.get('check_password')

        if password == r_password :
            myuser = User.objects.create_user(username , email, password)
            myuser.first_name = 'lolan'
            myuser.last_name = 'thangappan'

            myuser.save()
            messages.success(request,username)
            return redirect('signin')

    return render(request,"clone/signuppage.html")