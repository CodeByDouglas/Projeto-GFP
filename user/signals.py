from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Renda

@receiver(post_save, sender=User)
def criar_rendas_iniciais(sender, instance, created, **kwargs):

    """Cria 4 rendas vazias para cada novo usuário.

    Este sinal é executado toda vez que um novo usuário é criado. Ele cria 4
    rendas vazias para o novo usuário, com o nome "Renda" e valor 0. Isso
    facilita a vida do usuário, pois ele pode começar a preencher as rendas
    sem precisar criar uma renda vazia manualmente.

    """
    
    if created:
        # Cria 4 rendas vazias para cada novo usuário
        for i in range(4):
            Renda.objects.create(usuario=instance, nome_renda=f'Renda', valor_renda=0)

