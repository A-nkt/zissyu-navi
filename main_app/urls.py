from . import views
from django.urls import path

app_name="main_app"

urlpatterns = [
    path('',views.home,name='home'),
    path('form/',views.form,name='form'),
]
