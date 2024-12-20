"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from bookshelf.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth URLs
    path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    
    #Signup
    path("signup/", SignUpView.as_view(), name="signup"),
    
    #Login & Logout
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    #Passowrd Reset
            # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'), #For the password reset form.
            # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), #For confirmation after the form is submitted.
            # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'), #For entering a new password.
            # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), #For showing success.
    
    #Password Change
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
