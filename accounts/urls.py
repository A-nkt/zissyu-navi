from django.urls import path
from django.contrib.auth import views as google_auth_view

from . import views


app_name = "accounts"
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('create/', views.UserCreate.as_view(), name='create'),
    path('mypage/', views.MyPage, name='create'),
    path('mypage/about_email/', views.AboutEmailView.as_view(), name='about_email'),
    path('mypage/account_info/', views.AccountInfoView.as_view(), name='account_info'),
    path('mypage/comments/', views.Comment, name='comments'),
    path('mypage/user_info/', views.UserInfoView.as_view(), name='user_info'),
    path('mypage/password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('mypage/password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('mypage/exit/', views.Exit, name='exit'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('create/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
    path('user_create_done/', views.UserCreateDone.as_view(), name='user_create_done'),
    path('google/', views.google, name='google'),
    path('google_login/', google_auth_view.LoginView.as_view(), name='google_login'),
    path('google_logout/', google_auth_view.LogoutView.as_view(), name='google_logout'),
]
