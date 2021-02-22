from . import views
from django.urls import path

app_name="main_app"

urlpatterns = [
    path('',views.home,name='home'),
    path('form/',views.form,name='form'),
    path('search/',views.search,name='search'),
    path('list/',views.list,name='list'),
    path('footer-content/',views.footer_content,name='footer_content'),
    path('list/individual/',views.individual,name='individual'),
    path('list/individual/user_answer/',views.user_answer,name='user_answer'),
    path('list/individual/user_list/',views.user_list,name='user_list'),
    path('contact/',views.contact,name="contact"),
    path('user/',views.user,name='user'),
    path('mypage/',views.mypage,name='mypage'),
]
