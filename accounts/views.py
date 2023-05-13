import slackweb

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.template.loader import render_to_string
from django.http import HttpResponseBadRequest
from sendgrid.helpers.mail import Email, To, Content, Mail

from .forms import LoginForm, UserCreateForm, MyPasswordChangeForm, UsernameChangeForm, EmailChangeForm
from .sub_function import inte
from main_app.models import OtherRecord


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


class UserCreate(CreateView):
    template_name = 'accounts/create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        DEBUG = settings.DEBUG
        if DEBUG:
            subject = render_to_string('for_email_txt/subject.txt', context)
            message = render_to_string('for_email_txt/message_dev.txt', context)
            user.email_user(subject, message)
        else:
            subject = render_to_string('for_email_txt/subject.txt', context)
            message = render_to_string('for_email_txt/message.txt', context)
            from_email = Email("hospee.com@gmail.com")
            to_email = To(user.email)
            subject = subject
            content = Content("text/plain", message)
            mail = Mail(from_email, to_email, subject, content)
        return redirect('accounts:user_create_done')


class UserCreateDone(TemplateView):
    template_name = 'accounts/mypage/user_create_done.html'


class UserCreateComplete(TemplateView):
    template_name = 'accounts/mypage/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60 * 60 * 24)

    def get(self, request, **kwargs):
        token = kwargs.get('token')
        DEBUG = settings.DEBUG
        if not DEBUG:
            slack = slackweb.Slack(url="***")
            slack.notify(text="-----新規投稿のお知らせ-----" + '\n' + "新しいユーザーが作成されました")

        try:
            user_pk = loads(token, max_age=self.timeout_seconds)
        except SignatureExpired:
            return HttpResponseBadRequest()
        except BadSignature:
            return HttpResponseBadRequest()
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)
        return HttpResponseBadRequest()


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/mypage/logout.html'


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/mypage/password_change.html'


class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'accounts/mypage/password_change_done.html'


@login_required
def MyPage(request):
    user_obj = User.objects.get(username=request.user)
    year = str(user_obj.date_joined.year)
    month = inte(user_obj.date_joined.month)
    day = inte(user_obj.date_joined.day)
    date_joined = year + '年' + month + '月' + day + '日'
    context = {
        'date_joined': date_joined,
    }
    return render(request, 'accounts/mypage.html', context)


class AboutEmailView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/mypage/about_email.html'


class AccountInfoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        usernameform = UsernameChangeForm()
        emailform = EmailChangeForm()
        context = {
            'usernameform': usernameform,
            'emailform': emailform,
        }
        return render(request, 'accounts/mypage/account_info.html', context)

    def post(self, request, *args, **kwargs):
        try:
            form = UsernameChangeForm(request.POST)
            user_obj = User.objects.get(username=request.user)
            new_username = request.POST['username']
            user_obj.username = new_username
            OtherRecord.objects.all().filter(username=request.user).update(username=new_username)
            _type = "username"
        except:
            form = EmailChangeForm(request.POST)
            user_obj = User.objects.get(username=request.user)
            user_obj.email = request.POST['email']
            _type = "email"

        user_obj.save()
        return render(request, 'accounts/mypage/account_info_done.html', {'type': _type})


@login_required
def Exit(request):
    if len(request.POST) == 1:
        User.objects.filter(username=request.user).delete()
        return render(request, 'accounts/mypage/exit_done.html')
    return render(request, 'accounts/mypage/exit.html')


class UserInfoView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/mypage/user_info.html'


@login_required
def Comment(request):
    obj = OtherRecord.objects.all().filter(username=request.user)
    context = {
        'obj': obj,
    }
    return render(request, 'accounts/mypage/comments.html', context)


def google(request):
    return render(request, 'accounts/google.html')
