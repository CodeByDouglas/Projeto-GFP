from django.contrib.auth import login, authenticate
from .models import Usuario  # Para verificar a existência de usuários no banco de dados
from django.contrib import messages
from .forms import CadastroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.urls import path
#django.contrib.auth.views: Este módulo contém views prontas relacionadas à autenticação no Django. Essas views são genéricas e já fazem todo o trabalho pesado (como autenticar o usuário, validar senhas, redirecionar). 
#views as auth_views: Esse comando apenas renomeia o módulo views para auth_views. Para  evitar conflitos de nomes e também torna mais claro que estamos usando views relacionadas à autenticação.




#classe chamada CustomLoginView, que herda de LoginView, uma view genérica fornecida pelo Django.
#LoginView: view genérica do Django que já lida com o processo de login de usuários. Ela verifica as credenciais, autentica o usuário e o redireciona para uma página após o login, se for bem-sucedido.



class CustomLoginView(auth_views.LoginView):
    template_name = 'user/login.html'  # Template para o login
    redirect_authenticated_user = False  # Redireciona usuários já autenticados
    success_url = reverse_lazy('dashboard')  # Após login bem-sucedido, redireciona ao dashboard

@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html')  # Aqui você cria um template para o dashboard

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            
            # Verifica se o usuário já existe
            if Usuario.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já existe. Por favor, escolha outro.')
            else:
                user = form.save()  # Salva o usuário e o retorna
                
                # Autentica o usuário automaticamente
                login(request, user)  # Faz login automaticamente
                
                messages.success(request, 'Cadastro realizado com sucesso! Você foi logado automaticamente.')
                return redirect('dashboard')  # Redireciona para o dashboard após o login
    else:
        form = CadastroForm()
    
    return render(request, 'user/cadastro.html', {'form': form})

#Função cadastrar_usuario(request)
#def cadastrar_usuario(request)::
#Define a função que lida com a lógica de cadastro de usuários, recebendo a requisição HTTP como argumento.
#Verificando o Método da Requisição
#if request.method == 'POST'::
#Verifica se o método da requisição é POST, o que significa que os dados do formulário foram enviados para serem processados. Se for GET, a página de cadastro será exibida.
#Instanciando o Formulário
#form = CadastroForm(request.POST):
#
#Cria uma instância do formulário CadastroForm, passando os dados da requisição (request.POST) para processar os dados submetidos pelo usuário.
#if form.is_valid()::
#
#Verifica se os dados enviados no formulário são válidos, de acordo com as regras definidas no formulário (por exemplo, se os campos obrigatórios estão preenchidos e se as senhas são compatíveis).
#Verificando se o Usuário Já Existe
#username = form.cleaned_data.get('username'):
#
#Obtém o nome de usuário do formulário, acessando os dados limpos (dados que passaram pela validação do formulário).
#if Usuario.objects.filter(username=username).exists()::
#
#Verifica se já existe um usuário com o mesmo nome de usuário no banco de dados. Utiliza o método filter para buscar usuários com o mesmo username e exists() para retornar True se encontrar.
#messages.error(request, 'Nome de usuário já existe. Por favor, escolha outro.'):
#
#Se o usuário já existir, exibe uma mensagem de erro informando que o nome de usuário está em uso.
#Salvando o Usuário e Realizando o Login
#else::
#
#Caso o nome de usuário não exista, prossegue para salvar o novo usuário.
#user = form.save():
#
#Salva o usuário no banco de dados e retorna a instância do usuário recém-criado.
#login(request, user):
#
#Autentica o usuário recém-criado automaticamente, realizando o login no sistema.
#Exibindo Mensagem de Sucesso e Redirecionando
#messages.success(request, 'Cadastro realizado com sucesso! Você foi logado automaticamente.'):
#
#Exibe uma mensagem de sucesso, informando que o cadastro foi realizado e o usuário foi logado automaticamente.
#return redirect('dashboard'):
#
#Redireciona o usuário para o dashboard após o cadastro e login bem-sucedidos.
#Lidando com Requisições GET
#else: form = CadastroForm():
#
#Caso o método da requisição não seja POST, ou seja, se for um GET, uma nova instância do formulário CadastroForm é criada para ser exibida na página de cadastro.
#return render(request, 'user/cadastro.html', {'form': form}):
#
#Renderiza a página de cadastro (cadastro.html), passando o formulário para o template.
#Esse fluxo cuida tanto da exibição do formulário quanto da validação e criação de um novo usuário, além de realizar o login automaticamente após o cadastro.