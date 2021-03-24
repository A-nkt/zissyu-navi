from . import views
from django.urls import path

app_name="main_app"

urlpatterns = [
    path('about_us',views.about,name='about'),
]
