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

@login_required(login_url='signin')
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        # form.user = request.user
        if form.is_valid:
            form.user = request.user
            form.save()
            return redirect('signin')
    else:
        form = UploadFileForm()
    return render(request,'app/index.html',{
        'form' : form
        })

@login_required(login_url='signin')
def view_files(request):
    files = Document.objects.filter(user = request.user)
    print('out loop')
    print(files)
    for file in files:
        print('in loop')
        print(file.user)
    return render(request,'app/files.html',{
        'files':files
    })