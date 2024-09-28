from django.db import models


class Historico_gastos(models.Model):
    #Relaciona o histórico com o perfil do usuário, uma relação um-pra-muitos um perfil para varios resgistros.
    perfil = models.ForeignKey('conta.Perfil_de_usuario', related_name='historico_gastos', 
    on_delete=models.CASCADE )
    
    #Armazena o ano como um número inteiro.
    ano= models.IntegerField()
    
    #Aramzena o mês com um texto como Janeiro, Fevereiro etc ... 
    mes = models.CharField(max_length=20)

    #Armazena a renda que entrou no mês.
    total_renda= models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) :
        return f"{self.ano} - {self.mes}"
    
class Despesas(models.Model):
    
    #Define as categorias fixas das dispesas e uma lista de tuplas onde o primeiro valor é armazenado no banco de dados e o segundo valor e exibido para o usuário. 
    CATEGORIAS= [('mercado', 'Mercado'),
        ('transporte', 'Transporte'),
        ('saude', 'Saúde'),
        ('educacao', 'Educação'),
        ('habitacao', 'Habitação'),
        ('pessoais', 'Despesas Pessoais'),
        ('lazer', 'Lazer'),
        ('outros', 'Outros')]
    #Relaciona as despesas a um historico de gastos.
    historico= models.ForeignKey(Historico_gastos, related_name='despesas', on_delete=models.CASCADE)
    
    #Armazena o nome das despesas
    nome_da_despesa= models.CharField(max_length=100)
    
    #Aramazena o valor das despesas
    valor_da_despesa= models.DecimalField(max_digits=10, decimal_places=2)
    
    #Aramzena a categoria da despesa de acordo com a lista pré definida.
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    #Armazena data dia mes e ano individualmente para cada gasto para filtragens mais detalhadas.
    data_do_gasto = models.DateField()
    
    def __str__(self) :
        return f"{self.nome_da_despesa} - {self.valor_da_despesa} - {self.categoria} - {self.data_do_gasto}"
    

class Despesa_fixa(models.Model):
    despesa= models.OneToOneField(Despesas, on_delete=models.CASCADE)
    data_fim_fixa = models.DateField()

    def __str__(self) :
        return f"{self.Despesas.nome_do_gasto} - Fixa até {self.data_fim_fixa}"

class Despesa_prestação(models.Model):
    despesa= models.OneToOneField(Despesas, on_delete=models.CASCADE)
    quantidade_de_parcelas= models.IntegerField()

    def __str__(self):
        return f"{self.despesa.nome_do_gasto} - {self.quantidade_parcelas} parcelas"