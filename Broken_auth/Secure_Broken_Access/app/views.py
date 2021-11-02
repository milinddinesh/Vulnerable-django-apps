from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Document
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,"app/homepage.html")

#view for the signup page
def signup(request):
    #for the sign up form 
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

#view for the signin page
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        passw = request.POST['password']

        user = authenticate(username = username,password = passw)
        if user is not None:
            login(request,user)
            return redirect('index')
        else :
            messages.error(request,"Bad credentials!")
            return redirect('signin')
    return render(request,"app/loginpage.html")

#also the page where the upload happens.
@login_required(login_url='signin')
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid:
            saved_form = form.save(commit=False)
            saved_form.username = User.objects.get(username = request.user)
            print(saved_form.username)
            saved_form.save()
            return redirect('index')
    else:
        form = UploadFileForm()
    return render(request,'app/index.html',{
        'form' : form
        })

@login_required(login_url='signin')
def view_files(request):
    files = Document.objects.filter(username= request.user) #supposed to print the files of the current user but is not
    # files = Document.objects.all() #this works but prints all the files .
    print('out loop') #just to test
    #print(files)
    for file in files:
        print('in loop')
        print(file.username)
    return render(request,'app/files.html',{
        'files':files
    })