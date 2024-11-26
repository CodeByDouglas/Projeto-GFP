import ctypes
import os

# Carrega a DLL
dll_path = os.path.join(os.path.dirname(__file__), 'calculos.dll')
calculos = ctypes.CDLL(dll_path)

# Declara a função somaValores
calculos.somaValores.argtypes = (ctypes.POINTER(ctypes.c_float), ctypes.c_int)
calculos.somaValores.restype = ctypes.c_float

# Declara a função subtrairValores
calculos.subtrairValores.argtypes = (ctypes.c_float, ctypes.c_float)
calculos.subtrairValores.restype = ctypes.c_float

# Declara a função calcularPorcentagens
calculos.calcularPorcentagens.argtypes = (ctypes.POINTER(ctypes.c_float), ctypes.c_float)
calculos.calcularPorcentagens.restype = ctypes.POINTER(ctypes.c_float)

# Declara a função calcularParcelasRestantes
calculos.calcularParcelasRestantes.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int)
calculos.calcularParcelasRestantes.restype = ctypes.POINTER(ctypes.c_int)

# Declara a função liberarMemoria
calculos.liberarMemoria.argtypes = (ctypes.POINTER(ctypes.c_int),)
calculos.liberarMemoria.restype = None

# Função para somar valores em um array
def soma_valores(valores):
    # Obtém o tamanho do array
    tamanho = len(valores)
    # Define o tipo do array como um array de floats
    array_type = ctypes.c_float * tamanho
    # Converte a lista de valores para um array de floats
    valores_array = array_type(*valores)
    # Chama a função somaValores do módulo calculos e retorna o resultado
    return calculos.somaValores(valores_array, tamanho)

# Função para subtrair despesas da renda
def subtrair_valores(rendas, despesas):
    # Chama a função subtrairValores do módulo calculos e retorna o resultado
    return calculos.subtrairValores(despesas, rendas)

# Função para calcular porcentagens de valores por categoria
def calcular_porcentagens(valores, valor_total):
    # Obtém o tamanho do array
    tamanho = len(valores)
    # Define o tipo do array como um array de floats
    array_type = ctypes.c_float * tamanho
    # Converte a lista de valores para um array de floats
    valores_array = array_type(*valores)
    # Chama a função calcularPorcentagens do módulo calculos e obtém o ponteiro para o array de porcentagens
    porcentagens_ptr = calculos.calcularPorcentagens(valores_array, valor_total)
    # Converte o ponteiro para uma lista de porcentagens
    return [porcentagens_ptr[i] for i in range(tamanho)]

# Função para calcular o número de parcelas restantes
def calcular_parcelas_restantes(quantidade_parcelas, meses_inicio, anos_inicio, mes_atual, ano_atual):
    # Obtém o tamanho do array
    tamanho = len(quantidade_parcelas)
    # Define o tipo do array como um array de inteiros
    array_type_int = ctypes.c_int * tamanho
    # Converte as listas de quantidade de parcelas, meses de início e anos de início para arrays de inteiros
    quantidade_parcelas_array = array_type_int(*quantidade_parcelas)
    meses_inicio_array = array_type_int(*meses_inicio)
    anos_inicio_array = array_type_int(*anos_inicio)
    # Chama a função calcularParcelasRestantes do módulo calculos e obtém o ponteiro para o array de parcelas restantes
    parcelas_restantes_ptr = calculos.calcularParcelasRestantes(quantidade_parcelas_array, meses_inicio_array, anos_inicio_array, tamanho, mes_atual, ano_atual)
    # Converte o ponteiro para uma lista de parcelas restantes
    parcelas_restantes = [parcelas_restantes_ptr[i] for i in range(tamanho)]
    # Libera a memória alocada para o array de parcelas restantes
    calculos.liberarMemoria(parcelas_restantes_ptr)
    # Retorna a lista de parcelas restantes
    return parcelas_restantes