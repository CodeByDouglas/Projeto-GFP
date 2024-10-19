from .views import cadastrar_usuario
from django.urls import path
from .views import CustomLoginView
from .views import CustomLoginView, dashboard 
#from django.urls import path:importando a função path do Django, que é usada para definir mapeamentos de URLs para views.
#from .views import CustomLoginView:importamos a nossa CustomLoginView que criamos  na view. Isso permite que a gente use essa view para lidar com a URL de login.





#urlpatterns = []: O Django espera uma lista chamada urlpatterns que contém todos os mapeamentos de URLs para a aplicação.
#'login/': Define que a URL /login/ será usada para a página de login.
#CustomLoginView.as_view(): Isso é necessário porque CustomLoginView é uma classe, e precisamos transformá-la em uma função de view utilizável. O método as_view() faz isso.
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),  # URL para a página de login

    path('dashboard/', dashboard, name='dashboard'),  # URL do dashboard    
    
    path('cadastro/', cadastrar_usuario, name='cadastrar'), #URL do cadastro
]


