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
    return render(request,"app/index.html")



#function that handles the file upload feature
def upload_file(request):
    form = UploadFileForm(request.Post , request.Files)
    if form.is_valid :
        file_handle(request.FILES['file'])
        

def file_handle(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid :
            form.save()
            return redirect('index')
    else :form = UploadFileForm()
    return render(request,'app/index.html',{
        form : form 
    })

def upload_file(request):   
    context = {}
    upload_file = request.FILES['foo']
    fs = FileSystemStorage()
    #fs.save(upload_file.name,upload_file)
    name = fs.save(upload_file.name,upload_file)
    # document = FilesUpload.objects.create(file = upload_file)
    # document.save()
    print(upload_file.name)
    context['url']=fs.url(name)
    HttpResponse("Your file was uploaded")
    return render(request,"clone/index.html",context)

