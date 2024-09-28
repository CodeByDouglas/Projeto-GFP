from django.urls import path
from . import views

urlpatterns= [
    path('dashboard/', views.dashbord, name='dashboard'),#Define a URL dashboard/ e define também que quando acessada essa URL vai rodar a fução dashboard do Views. 



]