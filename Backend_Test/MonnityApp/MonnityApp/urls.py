"""MonnityApp URL Configuration"""
##Django
from django.contrib import admin
from django.urls import path, include
from users.views import signup_view
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

##Forms
from users.views import UserEditView, PasswordsChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/signup/', signup_view, name="signup"),
    path('users/profileupdate/', UserEditView.as_view(), name="profileupdate"),
    path('users/password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'),
        name="change_password")
]


