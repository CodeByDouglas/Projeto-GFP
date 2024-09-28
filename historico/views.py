from django.shortcuts import render
from django.contrib.auth.decorators import login_required #Importa o login_required que faz com que apenas user logodas possão acessar está página. 


@login_required #Garante que apenas user logados possam acessar. 
def dashbord(request):
    return render(request, 'dashboard.html') #Essa função e encarregada de carregar o html do dashbord.html mas apenas de usuários logados. 

