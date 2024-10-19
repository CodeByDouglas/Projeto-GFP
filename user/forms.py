from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Renda

class CadastroForm(UserCreationForm):
    nome_real = forms.CharField(max_length=100, required=True, label="Nome")
    nome_renda = forms.CharField(max_length=50, required=True, label="Renda")
    valor_renda = forms.DecimalField(max_digits=10, decimal_places=2, required=True, label="Valor")

    class Meta:
        model = Usuario
        fields = ['username', 'nome_real', 'password1', 'password2']

    def save(self, commit=True):
        # Salvando o usuário
        user = super().save(commit=False)
        user.nome_real = self.cleaned_data['nome_real']
        if commit:
            user.save()

        # Salvando a renda
        nome_renda = self.cleaned_data['nome_renda']
        valor_renda = self.cleaned_data['valor_renda']
        Renda.objects.create(usuario=user, nome_renda=nome_renda, valor_renda=valor_renda)
        
        return user

#*from django import forms:
#?Importa o módulo de formulários do Django, que fornece classes e ferramentas para criação e manipulação de formulários.

#*from django.contrib.auth.forms import UserCreationForm:
#?Importa a classe UserCreationForm, que é um formulário pronto do Django para lidar com a criação de novos usuários com campos de autenticação como username, password1 e password2.

#*from .models import Usuario, Renda:
#?Importa os modelos Usuario e Renda do arquivo models.py para que possam ser utilizados no formulário e no salvamento dos dados do usuário e de suas rendas.

#*Classe CadastroForm:
#*class CadastroForm(UserCreationForm)::
#?Define uma nova classe de formulário chamada CadastroForm que herda de UserCreationForm, o que significa que esse formulário inclui os campos padrões de criação de usuário do Django, mas permite estender o formulário para adicionar campos personalizados.

#*Campos do Formulário:
#*nome_real = forms.CharField(...):
#?Adiciona um campo de formulário nome_real que é um campo de texto obrigatório (CharField) para capturar o nome real do usuário.

#*nome_renda = forms.CharField(...):
#?Adiciona um campo de formulário nome_renda que é um campo de texto obrigatório para capturar o nome de uma renda associada ao usuário.

#*valor_renda = forms.DecimalField(...):
#?Adiciona um campo de formulário valor_renda que é um campo numérico decimal obrigatório para capturar o valor da renda.

#*Meta Classe:
#*class Meta::
#?A classe Meta define os metadados do formulário, como o modelo ao qual o formulário se aplica e os campos que devem ser incluídos.

#*model = Usuario:
#?Define que o modelo associado a esse formulário é o modelo Usuario.

#*fields = ['username', 'nome_real', 'password1', 'password2']:
#?Especifica que os campos que devem ser exibidos no formulário são: username, nome_real, password1 e password2.

#*Método save:
#*def save(self, commit=True)::
#?Este método sobrescreve o método save padrão do Django para salvar o usuário e os dados associados de forma personalizada.

#*user = super().save(commit=False):
#?Chama o método save da classe pai (UserCreationForm), criando uma instância do usuário, mas sem salvar ainda no banco de dados (commit=False).

#*user.nome_real = self.cleaned_data['nome_real']:
#?Define o campo nome_real do usuário com o valor que foi capturado no formulário e limpado.

#*if commit::
#?Verifica se a instância do usuário deve ser salva no banco de dados agora.

#*user.save():
#?Se o parâmetro commit for True, o usuário é salvo no banco de dados.
#?Salvando a Renda:

#*nome_renda = self.cleaned_data['nome_renda']:
#?Pega o nome da renda fornecido no formulário.

#*valor_renda = self.cleaned_data['valor_renda']:
#?Pega o valor da renda fornecido no formulário.

#*Renda.objects.create(usuario=user, nome_renda=nome_renda, valor_renda=valor_renda):
#?Cria e salva uma nova instância de Renda, associada ao usuário criado, com o nome e o valor da renda capturados no formulário.

#*return user:

#?Retorna a instância do usuário após salvar todos os dados no banco de dados.
#*Esse código faz a integração completa entre o formulário de cadastro de usuário e o modelo de usuário, além de associar as rendas ao usuário durante o processo de criação.