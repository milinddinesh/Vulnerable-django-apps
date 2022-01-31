from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from . import patch

# urlpatterns = [
#     path('',views.home, name = 'home'),
#     path('index',views.index,name = 'index'),
#     path('signin',views.signin,name = 'signin'),
#     path('files',views.view_files,name = 'view_files'),
#     path('signup',views.signup,name = 'signup'),
#     path('reset',views.reset,name='reset'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('',patch.home, name = 'home'),
    path('index',patch.index,name = 'index'),
    path('signin',patch.signin,name = 'signin'),
    path('files',patch.view_files,name = 'view_files'),
    path('signup',patch.signup,name = 'signup'),
    path('reset',patch.reset,name='reset'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)