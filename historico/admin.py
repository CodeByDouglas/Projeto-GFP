from django.contrib import admin
from .models import Historico_gastos, Despesas, Despesa_prestação, Despesa_fixa


#Registra os models no admin permite gerenciar as informações atravez da interface de administração do Django.

admin.site.register(Historico_gastos)
admin.site.register(Despesas)
admin.site.register(Despesa_prestação)
admin.site.register(Despesa_fixa)







