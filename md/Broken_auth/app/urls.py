from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('index',views.index,name = 'index'),
    path('signin',views.signin,name = 'signin'),
    path('files',views.view_files,name = 'view_files'),
    path('signup',views.signup,name = 'signup'),
    path('reset',views.reset,name='rest'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)