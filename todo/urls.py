"""TODO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from apps.tasks.views import *
from django.contrib.auth.views import LoginView
from apps.accounts.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    #! To avoid “social media fingerprinting” information leakage, host all images and your favicon on a separate domain.
    #! due to use of redirect_authenticated_user
    path('', LoginView.as_view(
        template_name='accounts/login.html', 
        redirect_authenticated_user=True,
        authentication_form = LoginForm,
        extra_context = {'page_name': 'Login'}
        ),
        name = 'login'
    ),
    path('tasks/', include('apps.tasks.urls', namespace='tasks')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    
]
