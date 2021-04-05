# Public Django
from django.shortcuts import render, redirect
from django.views.generic import  View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
# Public Python
# Private Django
from .forms import LoginForm,UserCreateForm
# Create your views here.
#class LoginView(LoginRequiredMixin,View):
class LoginView(View):
    def post(self, request, *arg, **kwargs):
        form = AuthenticationForm(data=request.POST, request=request)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password, request=request)
            login(request, user)
            return redirect('/')
        return render(request, 'accounts/login.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'accounts/login.html', {'form': form})

#アカウント作成
class CreateView(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password, request=request)
            login(request, user)
            return redirect('/')
        return render(request, 'accounts/create.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm()
        return  render(request, 'accounts/create.html', {'form': form})
