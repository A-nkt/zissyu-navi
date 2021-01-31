from . import views
from django.urls import path

app_name="main_app"

urlpatterns = [
    path('',views.home,name='home'),
    path('form/',views.form,name='form'),
    path('search/',views.search,name='search'),
    path('list/',views.list,name='list'),
    path('footer-content/',views.footer_content,name='footer_content'),
]
