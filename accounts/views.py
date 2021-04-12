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
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.template.loader import render_to_string
# Public Python
import sys
import slackweb
# Private Django
from .forms import LoginForm,UserCreateForm, MyPasswordChangeForm, UsernameChangeForm
from .sub_function import *
from main_app.models import OtherRecord
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
class UserCreate(CreateView):
    """ユーザー仮登録"""
    template_name = 'accounts/create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        """仮登録と本登録用メールの発行."""
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # アクティベーションURLの送付
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject = render_to_string('for_email_txt/subject.txt', context)
        message = render_to_string('for_email_txt/message.txt', context)

        user.email_user(subject, message)
        SENDGRID_API    = "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"

        sg          = sendgrid.SendGridAPIClient(api_key=SENDGRID_API)
        from_email  = Email("hospee.com@gmail.com")
        to_email    = To(user.email)
        subject     = subject
        content     = Content("text/plain", message)
        mail        = Mail(from_email, to_email, subject, content)
        response    = sg.client.mail.send.post(request_body=mail.get())
        return redirect('accounts:user_create_done')

class UserCreateDone(TemplateView):
    """ユーザー仮登録したよ"""
    template_name = 'accounts/mypage/user_create_done.html'

class UserCreateComplete(TemplateView):
    """メール内URLアクセス後のユーザー本登録"""
    template_name = 'accounts/mypage/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)  # デフォルトでは1日以内

    def get(self, request, **kwargs):
        """tokenが正しければ本登録."""
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)
        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest()
        # tokenが間違っている
        except BadSignature:
            return HttpResponseBadRequest()
        # tokenは問題なし
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    # 問題なければ本登録とする
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()

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


@login_required
def Comment(request):
    obj = OtherRecord.objects.all().filter(username=request.user)
    context = {
        'obj':obj,
    }
    return render(request,'accounts/mypage/comments.html',context)

import sendgrid
from sendgrid.helpers.mail import *

@login_required
def test_email(request):
    """
    SENDGRID_API    = "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"

    sg          = sendgrid.SendGridAPIClient(api_key=SENDGRID_API)
    from_email  = Email("hospee.com@gmail.com")
    #from_email  = Email("dsduoa31@gmail.com")
    to_email    = To("dsduoa31@gmail.com")
    subject     = "メールの件名"
    content     = Content("text/plain", "ここに本文")
    mail        = Mail(from_email, to_email, subject, content)
    response    = sg.client.mail.send.post(request_body=mail.get())
    """
    """題名"""
    subject = "題名"
    """本文"""
    message = "本文です\nこんにちは。メールを送信しました"
    """送信元メールアドレス"""
    from_email = "information@myproject"
    """宛先メールアドレス"""
    recipient_list = [
        "apptest@apptest.com"
    ]

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse("it is test.")
