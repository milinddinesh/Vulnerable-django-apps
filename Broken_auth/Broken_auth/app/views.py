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

#view for the signin page
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
            messages.error(request,"Bad credentials!")
            return redirect('signin')
    return render(request,"app/loginpage.html")

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('signin')
    else:
        form = UploadFileForm()
    return render(request,'app/index.html',{
        'form' : form
        })

def view_files(request):
    render(request,'app/files.html')

#not needed i guess
def upload(request):
    form = UploadFileForm()
    return render(request,'app/index.html',{
        form : form
    })