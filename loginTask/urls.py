from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('accounts.urls')), 
    path('accounts/', include('django.contrib.auth.urls')), 
    path('', lambda request: redirect('login')),
]
