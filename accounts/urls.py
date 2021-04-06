from . import views
from django.urls import path, include

app_name="accounts"

urlpatterns = [
    path('login/' ,views.LoginView.as_view(), name='login'),
    path('create/' ,views.CreateView.as_view(), name='create'),
    path('mypage/' ,views.MyPageView.as_view(), name='create'),
    path('logout/' ,views.CustomLogoutView.as_view(), name='logout'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
]
