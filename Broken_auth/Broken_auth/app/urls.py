from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.signin, name = 'signin'),
    path('index',views.index,name = 'index'),
    path('signin',views.signin,name = 'signin'),
    path('upload',views.upload,name = 'upload'),
    # path('upload_file',views.file_handle,name = 'file_handle'),
    # path('file_handle',views.file_handle,name='file_handle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)