# Public Django
from django.shortcuts import render, redirect
from django.views.generic import  View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import  TemplateView,DeleteView
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django_pandas.io import read_frame
from django.contrib.auth.decorators import login_required
# Public Python
import sys
# Private Django
from .forms import LoginForm,UserCreateForm, MyPasswordChangeForm, UsernameChangeForm
from .sub_function import *
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

class CustomLogoutView(LoginRequiredMixin,LogoutView):
    template_name = 'accounts/mypage/logout.html'

class PasswordChange(LoginRequiredMixin,PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/mypage/password_change.html'


class PasswordChangeDone(LoginRequiredMixin,PasswordChangeDoneView):
    template_name = 'accounts/mypage/password_change_done.html'

@login_required
def MyPage(request):
    user_obj = User.objects.get(username=request.user)
    year = str(user_obj.date_joined.year)
    month = inte(user_obj.date_joined.month)
    day = inte(user_obj.date_joined.day)
    date_joined = year + '年' + month + '月' + day + '日'

    context = {
        'date_joined':date_joined,
    }
    return render(request, 'accounts/mypage.html',context)

class AboutEmailView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/mypage/about_email.html'

class AccountInfoView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        form = UsernameChangeForm()
        return render(request, 'accounts/mypage/account_info.html', {'form': form})
    def post(self,request,*args,**kwargs):
        form = UsernameChangeForm(request.POST)
        if not form.is_valid:
            return render(request, 'main_app/form.html', {'form': form})
        user_obj = User.objects.get(username=request.user)
        user_obj.username = request.POST['username']
        user_obj.save()

        return render(request, 'accounts/mypage/account_info_done.html', {'form': form})

@login_required
def Exit(request):
    if len(request.POST) == 1:
        User.objects.filter(username=request.user).delete()
        return render(request, 'accounts/mypage/exit_done.html')
    return render(request, 'accounts/mypage/exit.html')

class UserInfoView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/mypage/user_info.html'

class CommentsView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/mypage/comments.html'
