from . import views
from django.urls import path, include

app_name="accounts"

urlpatterns = [
    path('login' ,views.LoginView.as_view(), name='login'),
    path('create' ,views.CreateView.as_view(), name='create'),
]
