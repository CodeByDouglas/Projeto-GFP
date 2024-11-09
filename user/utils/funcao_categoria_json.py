import json
from user.Calculos.calculos import soma_valores
from user.models import Despesa

def calcular_valores_por_categoria(usuario):
    # Obtém todas as despesas do usuário logado
    despesas = Despesa.objects.filter(usuario=usuario)
    
    # Inicializa um dicionário para armazenar os valores por categoria
    categorias = Despesa.CATEGORIA_DESPESA_CHOICES
    valores_por_categoria = {categoria: [] for categoria, _ in categorias}
    
    # Popula o dicionário com os valores das despesas
    for despesa in despesas:
        valores_por_categoria[despesa.categoria_despesa].append(despesa.valor_despesa)
    
    # Calcula o total por categoria usando a função soma_valores
    total_por_categoria = {categoria: soma_valores(valores) for categoria, valores in valores_por_categoria.items()}
    
    # Separa as categorias e os valores em dois arrays
    categorias_array = list(total_por_categoria.keys())
    valores_array = list(total_por_categoria.values())
    
    # Converte os arrays para JSON
    categorias_json = json.dumps(categorias_array)
    valores_json = json.dumps(valores_array)
    
    return categorias_json, valores_json