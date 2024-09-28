from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns= [ 
#Espesifica o nome da URL e o nome do templete que eu quero carregar.
#utiliza o view padrão de login do Django.
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name= 'login'),

#direciona o logout de volta para a página de login, ou seja quando o user apertar para sair da conta ele sera redirecionada novamente para o login.
     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 
]