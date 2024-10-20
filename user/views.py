from .models import Renda
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Despesa
from django.contrib.auth import login, authenticate #? login: Faz o login de um usuário autenticado, estabelecendo uma sessão.authenticate: Verifica as credenciais de um usuário (nome de usuário e senha).
from .models import Usuario  #? Importa o modelo Usuario definido no seu projeto para manipular os dados de usuários
from django.contrib import messages #? Utiliza o sistema de mensagens do Django para enviar notificações (sucesso, erro, etc.) ao usuário.
from .forms import CadastroForm,DespesaFixaForm, DespesaParceladaForm, DespesaComumForm #? Importa o formulário de cadastro definido no seu projeto, usado para registrar novos usuários e também os formularios de lançamentos de gastos.
from django.contrib.auth.decorators import login_required #? Decorador que impede o acesso a uma view por usuários não autenticados, redirecionando-os para a página de login.
from django.contrib.auth.views import LoginView #? Importa a view genérica de login do Django, que facilita a criação de uma página de login.
from django.urls import reverse_lazy #? Função que permite obter URLs de maneira atrasada (lazy), útil para redirecionamentos após operações como login ou logout.
from django.shortcuts import render, redirect #? render: Renderiza um template HTML com um contexto.redirect: Redireciona o usuário para uma URL específica.
from django.contrib.auth import views as auth_views #? Importa as views genéricas relacionadas à autenticação (como login, logout)
from django.urls import path #? Função usada para definir as rotas (URLs) da aplicação.




#?classe chamada CustomLoginView, que herda de LoginView, uma view genérica fornecida pelo Django.
#?LoginView: view genérica do Django que já lida com o processo de login de usuários. Ela verifica as credenciais, autentica o usuário e o redireciona para uma página após o login, se for bem-sucedido.

class CustomLoginView(auth_views.LoginView):
    template_name = 'user/login.html'  #? Template para o login
    success_url = reverse_lazy('dashboard')  #? Após login bem-sucedido, redireciona ao dashboard

@login_required 
def dashboard(request):
    return render(request, 'user/dashboard.html')  

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            
            if Usuario.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já existe. Por favor, escolha outro.')
            else:
                user = form.save()                  
                login(request, user)  
                
                messages.success(request, 'Cadastro realizado com sucesso! Você foi logado automaticamente.')
                return redirect('dashboard')  
    else:
        form = CadastroForm()
    
    return render(request, 'user/cadastro.html', {'form': form})
'''
#//TODO: Função cadastrar_usuario(request)
#* def cadastrar_usuario(request)::
#? Define a função que lida com a lógica de cadastro de usuários, recebendo a requisição HTTP como argumento.

#//TODO:Verificando o Método da Requisição
#* if request.method == 'POST'::
#? Verifica se o método da requisição é POST, o que significa que os dados do formulário foram enviados para serem processados. Se for GET, a página de cadastro será exibida.

##//TODO:Instanciando o Formulário
#* form = CadastroForm(request.POST):
#? Cria uma instância do formulário CadastroForm, passando os dados da requisição (request.POST) para processar os dados submetidos pelo usuário.

#* if form.is_valid()::
#? Verifica se os dados enviados no formulário são válidos, de acordo com as regras definidas no formulário (por exemplo, se os campos obrigatórios estão preenchidos e se as senhas são compatíveis).

#//TODO:verificando se o Usuário Já Existe
#* username = form.cleaned_data.get('username'):
#? Obtém o nome de usuário do formulário, acessando os dados limpos (dados que passaram pela validação do formulário).

#?* Usuario.objects.filter(username=username).exists()::
#? Verifica se já existe um usuário com o mesmo nome de usuário no banco de dados. Utiliza o método filter para buscar usuários com o mesmo username e exists() para retornar True se encontrar.

#* if Usuario.objects.filter(username=username).exists():
#? Verifica se o nome de usuário já existe no banco de dados.

#* messages.error(request, 'Nome de usuário já existe. Por favor, escolha outro.'):
#? Se o usuário já existir, exibe uma mensagem de erro informando que o nome de usuário está em uso.

#//TODO:Salvando o Usuário e Realizando o Login
#* else:
#?Caso o nome de usuário não exista, prossegue para salvar o novo usuário.

#* user = form.save():
#? Salva o usuário no banco de dados e retorna a instância do usuário recém-criado.

#* login(request, user):
#? Autentica o usuário recém-criado automaticamente, realizando o login no sistema.

#* messages.success(request, 'Cadastro realizado com sucesso! Você foi logado automaticamente.'):
#? Exibe uma mensagem de sucesso, informando que o cadastro foi realizado e o usuário foi logado automaticamente.

#* return redirect('dashboard'):
#? Redireciona o usuário para o dashboard após o cadastro e login bem-sucedidos.

#//TODO: Lidando com Requisições GET
#* else: form = CadastroForm():
#? Caso o método da requisição não seja POST, ou seja, se for um GET, uma nova instância do formulário CadastroForm é criada para ser exibida na página de cadastro.

#*return render(request, 'user/cadastro.html', {'form': form}):
#? Renderiza a página de cadastro (cadastro.html), passando o formulário para o template.

#//TODO:Esse fluxo cuida tanto da exibição do formulário quanto da validação e criação de um novo usuário, além de realizar o login automaticamente após o cadastro.
'''
@login_required
def lancar_despesa_fixa(request):
    if request.method == 'POST':
        form = DespesaFixaForm(request.POST)
        if form.is_valid():
            despesa = form.save(commit=False)  
            despesa.usuario = request.user
            despesa.tipo_despesa = 'fixa'      
            despesa.save()             
            messages.success(request, 'Despesa lançada com sucesso!')
    else:
        form = DespesaFixaForm()
    return render(request, 'user/despesa_fixa.html', {'form': form})

@login_required
def lancar_despesa_parcelada(request):
    if request.method == 'POST':
        form = DespesaParceladaForm(request.POST)
        if form.is_valid():
            despesa = form.save(commit=False)  
            despesa.usuario = request.user
            despesa.tipo_despesa = 'parcelada'      
            despesa.save()             
            messages.success(request, 'Despesa lançada com sucesso!')
    
    else:
        form = DespesaParceladaForm()
    return render(request, 'user/despesa_parcelada.html', {'form': form})

@login_required
def lancar_despesa_comum(request):
    if request.method == 'POST':
        form = DespesaComumForm(request.POST)
        if form.is_valid():
            despesa = form.save(commit=False)  
            despesa.usuario = request.user
            despesa.tipo_despesa = 'ocasional'      
            despesa.save()             
            messages.success(request, 'Despesa lançada com sucesso!')
    else:
        form = DespesaComumForm()
    return render(request, 'user/despesa_comum.html', {'form': form})

def perfil(request):
    user = request.user
    rendas = user.rendas.all()  # Pega todas as rendas associadas ao usuário
    context = {
        'user': user,
        'rendas': rendas,  # Passa a lista de rendas para o contexto
    }
    return render(request, 'user/perfil.html', context)




