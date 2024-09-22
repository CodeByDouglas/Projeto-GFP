from django.db import models
from django.contrib.auth.models import User 
#inportando o sistema de gerenciamento de usuários padrão do Django

#Classe de do perfil do usuário.
class Perfil_de_usuario(models.Model):
    #Defini uma relação de um-pra-um do perfil com o a tabela de usuário, também define que caso o user seja deletado o perfil tmb vai ser deletado.
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    #Campo onde e guardado o nome do perfil, o tamanho maximo de nome foi definido para 100 caracters.
    nome= models.CharField(max_length=100)

    #função para que o nome do campo exibido seja o nome do perfil do usuário.
    def __str__(self):
        return self.nome

#Classe que armazena as rendas do usuário.
class Renda(models.Model):
    #Define uma relação de um-pra-muitos com a tabela de perfil do user, ou seja um perfil pode ter mais de uma renda associada a ele, também permite que atrávez da tabela de perfil possa de acessar as rendas do usuário com perfil.rendas.all() e também garante a exclusão caso o perfil do user seja excluido. 
    perfil=models.ForeignKey(Perfil_de_usuario, related_name='rendas', on_delete=models.CASCADE)
    
    #Campo de texto que armazena o nome da renda em no máximo 100 caractrs.
    nome_da_renda= models.CharField(max_length=100)

    #Campo númerico decimal qeu armazena  o valor da renda com duas casas decimais e com o número de no máximo 10 digitos. 
    valor_da_renda= models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) :
        return f"{self.nome_da_renda} - {self.valor_da_renda}"
