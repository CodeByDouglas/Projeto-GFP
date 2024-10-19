from django.contrib import admin
from .models import Usuario, Renda, Despesa #? Faz a inportação dos models que eu quero adicionar a interface de admin.


#?Registra o modelo de Usuario, renda e Despesa na interface de administração do Django.

admin.site.register(Usuario)

admin.site.register(Renda)

admin.site.register(Despesa)