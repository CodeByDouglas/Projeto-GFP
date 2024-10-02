from django import forms #importa o módulo de formularios do Django.
from django.contrib.auth.models import User #Inporta o model padrão de user do Django, Esse modelo lida com as funcionalidades principais de autenticação, como login, criação de contas, e armazenamento de senhas.
from django.contrib.auth.forms import UserCreationForm #Importa o formulário de cadastro padrão do Django.
from .models import Perfil_de_usuario, Renda #Importa os models Perfil_de_usuario e renda do app conta. 

#Definimos um nova classe chamada RegistroForm herda do formulário de criação de usuarios padrão do Django UserCreationForm, ou seja estamos adicinando novos campos ao formulário padrão.
class RegistroForm(UserCreationForm):
    nome= forms.CharField(max_length=100, required=True) #campo que recebe o nome do user, aceita até 100 caracters e é um campo obrigatório.
    nome_da_renda= forms.CharField(max_length=100, required=True)#campo que recebe o nome da renda, aceita ara 100 caracters e também e um campo obrigatório.
    valor_da_renda= forms.DecimalField(max_digits=10, decimal_places=2, required=True) #campo que recebe o valor da renda, recebe até 10 digitos sendo 2 desses digitos após a vírgula, também é um campo obrigatório. 

#Aqui temos algumas definições como em qual modelo está baseado e quais campos serão exibidos. 
class Meta:
    #Definimos que este fomulário está baseado no modelo User do Django. Assim, os campos relacionados ao usuário(como  nome de usuário e senha)serão gerenciados por este modelo.
    model = User
    
    #Aqui definimos os campos que vão ser exibidos no formulário. 
    fields = ['username', 'password1', 'password2', 'nome', 'nome_da_renda', 'valor_da_renda']

#Modificamos o metodo save para que ele também salve as informações adicionais(nome, renda, etc..) no banco de dados.
def save(self, commit=True):
    user = super(RegistroForm, self)#TIREI O COMIT FALSE AGORA A FUNÇÃO FOI RECONHECIDA E CIROU AS TABELAS. 
    user.save()

    print("Usuário criado: {use.username}")


    perfil = Perfil_de_usuario(user=user, nome=self.cleaned_data['nome'])
    perfil.save()
    print(f"Perfil criado para o usuário: {perfil.nome}")
    
    renda = Renda(perfil, nome_da_renda=self.cleaned_data['nome_da_renda'], valor_da_renda=self.cleaned_data['valor_da_renda'])
    renda.save()

    print(f"Renda associada: {renda.nome_da_renda}, {renda.valor_da_renda}")
    #Retorna o usuário criado, oque pode ser ultil para manter o fluxo e logar o usuário automaticamente após o cadastro.
    return user