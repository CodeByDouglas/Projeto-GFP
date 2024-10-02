from django.shortcuts import render, redirect #Importa a funções para renderizar templates e redirecionar URLs
from django.contrib.auth import login #importa a função de login do Django para automaticamente após o cadastro
from .forms import RegistroForm # Importa o formulário de cadastro que criamos no forms.py

def cadastro_usuario(request):
    if request.method == 'POST': #Verifica se a requisição HTPP é um POST(Quando o formulário e enviado)
        form = RegistroForm(request.POST) #instancia o formulário com os dados enviados pelo post
        if form.is_valid(): #Verifica se os dados do vormulário são valídos ou sejá se seguem as regras do formulário.
            user = form.save()#Aqui criamos uma variavel chamada user onde dentro dela foi chamada a função de save que salva todas as informações do formulario no banco de dados e retorna o objeto User recem criado(Isso foi definino no forms.py) que fica salvo dentro desta variável.
            login(request, user) # Loga o user automaticamente após o cadastro, passando como parametro a variável user que possui o usuário recem criado armazenado nela. 
            return redirect('dashboard')#Redireciona o usuário automaticamente para a página do dashboard após o cadastro. 
    else: 
        form = RegistroForm() #Se a Requisição for  GET ou sejá o acesso inicial a pagina ele cria um formulário vazio. 
    
    return render(request, 'cadastro.html', {'form': form}) #renderiza a página de cadastro e passa o formulário para o template.