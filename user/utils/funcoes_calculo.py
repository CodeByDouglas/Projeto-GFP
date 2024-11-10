import json
import datetime
from user.Calculos.calculos import calcular_porcentagens, soma_valores, calcular_parcelas_restantes
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

def calcular_porcentagem_por_categoria(usuario):
    # Obtém todas as despesas do usuário logado
    despesas = Despesa.objects.filter(usuario=usuario)
    
    # Inicializa um dicionário para armazenar os valores por categoria
    categorias = Despesa.CATEGORIA_DESPESA_CHOICES
    valores_por_categoria = {categoria: 0 for categoria, _ in categorias}
    
    # Popula o dicionário com os valores das despesas
    for despesa in despesas:
        valores_por_categoria[despesa.categoria_despesa] += despesa.valor_despesa
    
    # Separa as categorias e os valores em dois arrays
    categorias_array = list(valores_por_categoria.keys())
    valores_array = list(valores_por_categoria.values())
    
    # Calcula o valor total das despesas
    valor_total = sum(valores_array)
    
    # Calcula as porcentagens usando a função calcular_porcentagens
    porcentagens = calcular_porcentagens(valores_array, valor_total)
    
    # Converte os arrays para JSON
    categorias_json = json.dumps(categorias_array)
    porcentagens_json = json.dumps(porcentagens)
    
    return categorias_json, porcentagens_json

def calcular_prestacoes_restantes(usuario):
    # Obtém todas as despesas parceladas do usuário logado
    despesas_parceladas = Despesa.objects.filter(usuario=usuario, tipo_despesa='parcelada')
    
    # Inicializa listas para armazenar os resultados
    nomes_despesas = []
    parcelas_restantes_list = []
    parcelas_pagas_list = []
    datas_finais_list = []
    parcelas_formatadas_list = []
    
    # Coleta os dados necessários para calcular as parcelas restantes
    quantidade_parcelas = [despesa.parcelas for despesa in despesas_parceladas]
    anos_inicio = [despesa.data_despesa.year for despesa in despesas_parceladas]
    meses_inicio = [despesa.data_despesa.month for despesa in despesas_parceladas]
    mes_atual = datetime.datetime.now().month
    ano_atual = datetime.datetime.now().year
    
    # Calcula as parcelas restantes usando a função calcular_parcelas_restantes
    parcelas_restantes = calcular_parcelas_restantes(quantidade_parcelas, meses_inicio, anos_inicio, mes_atual, ano_atual)
    
    # Popula as listas com os resultados
    for despesa, parcelas_restantes in zip(despesas_parceladas, parcelas_restantes):
        nomes_despesas.append(despesa.nome_despesa)
        parcelas_restantes_list.append(parcelas_restantes)
        parcelas_pagas = despesa.parcelas - parcelas_restantes
        parcelas_pagas_list.append(parcelas_pagas)
        parcelas_formatadas_list.append(f"{parcelas_pagas}/{despesa.parcelas}")
        
        # Calcula a data final da prestação
        mes_final = (despesa.data_despesa.month + despesa.parcelas - 1) % 12 + 1
        ano_final = despesa.data_despesa.year + (despesa.data_despesa.month + despesa.parcelas - 1) // 12
        datas_finais_list.append(f"{mes_final}/{ano_final}")
    
    return nomes_despesas, parcelas_restantes_list, parcelas_formatadas_list, datas_finais_list

def calcular_despesas_fixas(usuario):
    # Obtém todas as despesas fixas do usuário logado
    despesas_fixas = Despesa.objects.filter(usuario=usuario, tipo_despesa='fixa')
    
    # Inicializa listas para armazenar os resultados
    nomes_despesas = []
    valores_despesas = []
    
    # Popula as listas com os resultados
    for despesa in despesas_fixas:
        nomes_despesas.append(despesa.nome_despesa)
        valores_despesas.append(despesa.valor_despesa)
    
    # Calcula o valor total das despesas fixas usando a função soma_valores
    valor_total = soma_valores(valores_despesas)
    
    return nomes_despesas, valores_despesas, valor_total