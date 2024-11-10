import json
import datetime
from user.Calculos.calculos import calcular_porcentagens, soma_valores, calcular_parcelas_restantes, subtrair_valores
from user.models import Despesa, Renda

def calcular_valores_por_categoria(usuario):
    # Obtém o mês e ano atual
    hoje = datetime.date.today()
    mes_atual = hoje.month
    ano_atual = hoje.year
    
    # Obtém todas as despesas do usuário logado no mês atual
    despesas = Despesa.objects.filter(usuario=usuario, data_despesa__year=ano_atual, data_despesa__month=mes_atual)
    
    # Inicializa dicionários para armazenar os valores por categoria
    valores_por_categoria = {}
    
    # Popula os dicionários com os resultados
    for despesa in despesas:
        categoria = despesa.categoria_despesa
        valor = float(despesa.valor_despesa)  # Converte Decimal para float
        if categoria in valores_por_categoria:
            valores_por_categoria[categoria] += valor
        else:
            valores_por_categoria[categoria] = valor
    
    # Converte os dicionários para listas de rótulos e valores
    categorias = list(valores_por_categoria.keys())
    valores = list(valores_por_categoria.values())
    
    # Converte as listas para JSON
    categorias_json = json.dumps(categorias)
    valores_json = json.dumps(valores)
    
    return categorias_json, valores_json

def calcular_porcentagem_por_categoria(usuario):
    # Obtém o mês e ano atual
    hoje = datetime.date.today()
    mes_atual = hoje.month
    ano_atual = hoje.year
    
    # Obtém todas as despesas do usuário logado no mês atual
    despesas = Despesa.objects.filter(usuario=usuario, data_despesa__year=ano_atual, data_despesa__month=mes_atual)
    
    # Inicializa um dicionário para armazenar os valores por categoria
    categorias = Despesa.CATEGORIA_DESPESA_CHOICES
    valores_por_categoria = {categoria: 0 for categoria, _ in categorias}
    
    # Popula o dicionário com os valores das despesas
    for despesa in despesas:
        valores_por_categoria[despesa.categoria_despesa] += float(despesa.valor_despesa)  # Converte Decimal para float
    
    # Calcula o total das despesas
    total_despesas = sum(valores_por_categoria.values())
    
    # Calcula a porcentagem de cada categoria
    porcentagens_por_categoria = {categoria: (valor / total_despesas) * 100 if total_despesas > 0 else 0 for categoria, valor in valores_por_categoria.items()}
    
    # Converte os dicionários para listas de rótulos e valores
    categorias = list(porcentagens_por_categoria.keys())
    porcentagens = list(porcentagens_por_categoria.values())
    
    # Converte as listas para JSON
    categorias_porcentagem_json = json.dumps(categorias)
    porcentagens_json = json.dumps(porcentagens)
    
    return categorias_porcentagem_json, porcentagens_json

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

def calcular_totais(usuario):
    # Obtém o mês e ano atual
    hoje = datetime.date.today()
    mes_atual = hoje.month
    ano_atual = hoje.year
    
    # Obtém todas as despesas do usuário logado no mês atual
    despesas = Despesa.objects.filter(usuario=usuario, data_despesa__year=ano_atual, data_despesa__month=mes_atual)
    valores_despesas = [float(despesa.valor_despesa) for despesa in despesas]  # Converte Decimal para float
    
    # Calcula o total das despesas usando a função soma_valores
    total_despesas = soma_valores(valores_despesas)
    
    # Obtém todas as rendas do usuário logado
    rendas = Renda.objects.filter(usuario=usuario)
    valores_rendas = [float(renda.valor_renda) for renda in rendas]  # Converte Decimal para float
    
    # Calcula o total das rendas usando a função soma_valores
    total_rendas = soma_valores(valores_rendas)
    
    # Calcula o saldo atual usando a função subtrair_valores
    saldo_atual = subtrair_valores(total_rendas, total_despesas)
    
    return total_despesas, total_rendas, saldo_atual