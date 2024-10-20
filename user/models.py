from django.core.validators import MinValueValidator
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser #?Importa o modelo AbstractUser, que é uma classe base usada para criar um modelo de usuário personalizado no Django.



#?class Usuario(AbstractUser): Aqui, criamos a classe Usuario que herda de AbstractUser. Isso permite que a gente estenda o modelo de usuário padrão do Django e adicione novos campos (como nome_real), mantendo todas as funcionalidades de autenticação
class Usuario(AbstractUser):
    nome_real = models.CharField(max_length=100)
    USERNAME_FIELD = 'username' #?USERNAME_FIELD = 'username'estamos definindo que o campo username continua sendo o campo de login padrão.
    
    def __str__(self):
        return self.username




#?class Renda(models.Model): Definimos a classe Renda que herda de models.Model, indicando que ela representa uma tabela no banco de dados.
class Renda(models.Model):
    
    #? usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='rendas'): Este campo define um relacionamento muitos-para-um entre Renda e Usuario. Ou seja, um usuário pode ter várias rendas.
    #? O ForeignKey cria esse relacionamento, e o parâmetro on_delete=models.CASCADE significa que, se o usuário for excluído, todas as rendas associadas a ele também serão excluídas.
    #*!O parâmetro related_name='rendas' permite que acessemos as rendas de um usuário usando user.rendas.all(). 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='rendas')
    
    nome_renda = models.CharField(max_length=50)
    valor_renda = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    #? def __str__(self): Define a representação em string do objeto Renda, retornando o nome da renda e o valor dela.
    def __str__(self):
        return f"{self.nome_renda} - {self.valor_renda}"




#?class Despesa(models.Model): Define a classe Despesa, representando uma tabela no banco de dados para armazenar despesas.
class Despesa(models.Model):
    
    TIPO_DESPESA_CHOICES = [
        ('ocasional', 'Ocasional'),
        ('fixa', 'Fixa'),
        ('parcelada', 'Parcelada')
    ]
    #? CATEGORIA_DESPESA_CHOICES: Uma lista de tuplas que define as opções de categorias para as despesas (mercado, transporte, saúde, etc.).
    CATEGORIA_DESPESA_CHOICES = [
        ('mercado', 'Mercado'),
        ('transporte', 'Transporte'),
        ('saude', 'Saúde'),
        ('educacao', 'Educação'),
        ('habitacao', 'Habitação'),
        ('pessoais', 'Despesas Pessoais'),
        ('lazer', 'Lazer'),
        ('outros', 'Outros'),
    ]
    #? usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='despesas'): Relaciona a despesa a um usuário. Isso significa que cada despesa está vinculada a um usuário específico
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='despesas')
    nome_despesa= models.CharField(max_length=50)
    tipo_despesa = models.CharField(max_length=10, choices=TIPO_DESPESA_CHOICES)
    valor_despesa = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    data_despesa = models.DateField(default=timezone.now)
    categoria_despesa = models.CharField(max_length=20, choices=CATEGORIA_DESPESA_CHOICES)
    data_final = models.DateField(null=True, blank=True)  # Para despesas fixas
    parcelas = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])  # Para despesas parceladas
    
    def __str__(self):
        return f"{self.nome_despesa} - {self.categoria_despesa}"
