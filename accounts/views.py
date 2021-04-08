# Public Django
from django.shortcuts import render, redirect
from django.views.generic import  View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import  TemplateView
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
# Public Python
import sys
# Private Django
from .forms import LoginForm,UserCreateForm, MyPasswordChangeForm
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
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,email=email ,password=password, request=request)
            login(request, user)
            return redirect('/')
        return render(request, 'accounts/create.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm()
        return  render(request, 'accounts/create.html', {'form': form})

class CustomLogoutView(LogoutView):
    template_name = 'accounts/mypage/logout.html'

class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/mypage/password_change.html'


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/mypage/password_change_done.html'

class MyPageView(TemplateView):
    template_name = 'accounts/mypage.html'

class AboutEmailView(TemplateView):
    template_name = 'accounts/mypage/about_email.html'

class UserInfoView(TemplateView):
    template_name = 'accounts/mypage/user_info.html'

class ExitView(TemplateView):
    template_name = 'accounts/mypage/exit.html'
