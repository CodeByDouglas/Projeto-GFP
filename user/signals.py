from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Renda

@receiver(post_save, sender=User)
def criar_rendas_iniciais(sender, instance, created, **kwargs):
    if created:
        # Cria 4 rendas vazias para cada novo usuário
        for i in range(4):
            Renda.objects.create(usuario=instance, nome_renda=f'Renda', valor_renda=0)
