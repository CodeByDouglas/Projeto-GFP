from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),#inportação padrão da URL adiministrativa.
    path('conta/', include('conta.urls')), #Incluindo as URLS criadas no app conta para as URLS gerais do projeto 
    path('', lambda request: redirect('login')), #Faz com que o Django redirecione automaticamente a URL raiz (/) para a página de login. A função lambda recebe o request http e o redireciona para o URL da page de login. 
    path('historico/', include('historico.urls'))#inclui as URLS do app historico .
]
