"""MonnityApp URL Configuration"""
##Django
#from django.contrib import admin
#from django.urls import path, include
#from django.views.generic.base import TemplateView

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('users/', include('users.urls')),
#    path('', TemplateView.as_view(template_name='home.html'), name='home'),
#]

from django.contrib import admin
from django.urls import path, include
from users.views import signup_view
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/signup/', signup_view, name="signup")
]


