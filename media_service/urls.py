from . import views
from django.urls import path

app_name="media_service"

urlpatterns = [
    path('',views.main,name='main'),
    path('making_now',views.making_now,name='making_now_url'),
]
