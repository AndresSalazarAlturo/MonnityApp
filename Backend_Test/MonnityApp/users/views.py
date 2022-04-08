"""Users views"""
###Django
#from django.shortcuts import render
#from django.contrib.auth import login, authenticate
#from .forms import SignUpForm
#from django.shortcuts import render, redirect
#
#
#def signup_view(request):
#    form = SignUpForm(request.POST)
#    if form.is_valid():
#        form.save()
#        username = form.cleaned_data.get('username')
#        password = form.cleaned_data.get('password1')
#        user = authenticate(username=username, password=password)
#        login(request, user)
#        return redirect('home')
#    else:
#        form = SignUpForm()
#    return render(request, 'signup.html', {'form': form})
#
####Anterior funciona######
##Django
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserChangeForm

def home(request):
    return render(request, 'home')

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = './updateUser.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


