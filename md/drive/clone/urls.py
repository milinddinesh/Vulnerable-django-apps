from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('signin',views.signin, name = 'signin'),
    path('signup',views.signup,name = 'signup'),
    path('index',views.index,name = 'index'),
    path('user_config',views.configPage,name = 'user_config'),
    path('upload_file',views.upload_file,name='upload_file')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

