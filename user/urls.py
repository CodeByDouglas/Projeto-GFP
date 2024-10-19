from django.urls import path#?from django.urls import path:importando a função path do Django, que é usada para definir mapeamentos de URLs para views.
from .views import CustomLoginView, dashboard, cadastrar_usuario #?from .views import CustomLoginView: Importamos a nossa CustomLoginView que criamos na view. Isso permite que a gente use essa view para lidar com a URL de login, E também a view dashboard que carrega o template da Home page, E a view de cadastro de usuário que é a view responsavel por salvar o usuário no database.







#?urlpatterns = []: O Django espera uma lista chamada urlpatterns que contém todos os mapeamentos de URLs para a aplicação.
urlpatterns = [
    #?CustomLoginView.as_view(): Isso é necessário porque CustomLoginView é uma classe, e precisamos transformá-la em uma função de view utilizável. O método as_view() faz isso.
    path('login/', CustomLoginView.as_view(), name='login'),  #?'login/': Define que a URL /login/ será usada para a página de login.

    path('dashboard/', dashboard, name='dashboard'),  #? URL do dashboard    
    
    path('cadastro/', cadastrar_usuario, name='cadastrar'), #? URL do cadastro
]


