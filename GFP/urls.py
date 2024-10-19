from django.contrib import admin #?Importa o módulo 'admin' do Django. Isso é necessário para adicionar as URLs da administração do Django ao projeto.
from django.urls import path, include #? Importa as funções 'path' e 'include' do Django. A função 'path' é usada para definir rotas de URLs, e 'include' permite que você adicione outras URLs de diferentes aplicações.
from user.views import CustomLoginView  #?Importa a view 'CustomLoginView' do módulo 'views' da aplicação 'user'.view criada para a página de login.


#? Define a lista de rotas de URLs que o Django deve seguir.
urlpatterns = [
    path('admin/', admin.site.urls),
    #? Define a rota para a área administrativa do Django. A URL 'admin/' é usada para acessar o painel de administração.
    
    path('', include('user.urls')),
    #? Inclui todas as URLs da aplicação 'user'. Isso significa que todas as rotas definidas em 'user/urls.py' serão incluídas no projeto principal.
      
      path('', CustomLoginView.as_view(), name='login'),  
    #? Define a rota para a página de login. Quando o usuário acessa a URL raiz (''), a view 'CustomLoginView' será exibida. 
    #? O nome 'login' é um identificador para essa URL, que pode ser usado em templates e redirecionamentos.
]
