import re
from urllib import response
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Document
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import Group


def home(request):
    return render(request,"app/homepage.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        r_password = request.POST.get('check_password')

        if password == r_password :
            myuser = User.objects.create_user(username , email, password)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            messages.success(request,"User created successfully")
            return redirect('signin')

    return render(request,"app/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        passw = request.POST['password']

        user = authenticate(username = username,password = passw)
        if user is not None:
            login(request,user)
            response = HttpResponse()
            form = UploadFileForm()
            response = render(request,'app/index.html',{
        'form' : form
        })
            response.set_cookie('id',request.user.id)
            response.set_cookie('uname',request.user)
            return response
        else :
            messages.error(request,"Bad credentials!")
            return redirect('signin')
    return render(request,"app/loginpage.html")

@login_required(login_url='signin') 
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid:
            saved_form = form.save(commit=False)
            saved_form.username = User.objects.get(username = request.user) 
            saved_form.save()
            return redirect('index')
    else:
        form = UploadFileForm()
    return render(request,'app/index.html',{
        'form' : form
        })

@login_required(login_url='signin')
def view_files(request):
    files = Document.objects.filter(username= request.user) 
    return render(request,'app/files.html',{
        'files':files
    })
    
@login_required(login_url='signin')
def reset(request):
    if request.method == 'POST':
        if request.COOKIES['id'] == '3' and request.COOKIES['uname'] == 'admin':
            if request.user.is_authenticated():
                uname = request.POST['username']
                try:
                    user = User.objects.get(username = uname)
                    return render(request,"app/reset.html")
                except User.DoesNotExist:
                    messages.error(request,"Account with username does not exist.")
                    return render(request,"app/reset.html")
            else : return render(request,"app/403.html")
        else :
            return render(request,"app/403.html")
    else :
        if request.COOKIES['id'] == '3' and request.COOKIES['uname'] == 'admin':
            return render(request,"app/reset.html")
        else : 
            return render(request,"app/403.html")
            