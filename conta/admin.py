from django.contrib import admin
from .models import Perfil_de_usuario, Renda

#Registra os models no admin permite gerenciar as informações atravez da interface de administração do Django.
admin.site.register(Perfil_de_usuario)
admin.site.register(Renda)

