from django.urls import path

from . import views

app_name = "media_service"

urlpatterns = [
    path('', views.main, name='main_url'),
    path('<int:id>', views.content, name='content_url'),
    path('making_now', views.making_now, name='making_now_url'),
    path('category', views.category, name='category'),
]
