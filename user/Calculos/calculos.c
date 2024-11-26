#include <stdio.h>
#include <stdlib.h>

// Função para somar valores em um array
__declspec(dllexport) float somaValores(float valores[], int tamanho) {
    float soma = 0.0;
    for (int i = 0; i < tamanho; i++) {
        soma += valores[i];
    }
    return soma;
}

// Função para subtrair despesas da renda
__declspec(dllexport) float subtrairValores(float despesas, float renda) {
    return renda - despesas;
}

// Função para calcular porcentagens de valores por categoria
__declspec(dllexport) float* calcularPorcentagens(float valorPorCategoria[8], float valorTotal) {
    static float porcentagens[8];
    for (int i = 0; i < 8; i++) {
        porcentagens[i] = (valorPorCategoria[i] / valorTotal) * 100;
    }
    return porcentagens;
}

// Função para calcular o número de parcelas restantes
__declspec(dllexport) int* calcularParcelasRestantes(int quantidadeParcelas[], int mesesInicio[], int anosInicio[], int tamanho, int mesAtual, int anoAtual) {
    // Aloca memória para armazenar as parcelas restantes
    int* parcelasRestantes = (int*)malloc(tamanho * sizeof(int));
    for (int i = 0; i < tamanho; i++) {
        // Calcula o número de meses passados desde o início da despesa
        int mesesPassados = (anoAtual - anosInicio[i]) * 12 + (mesAtual - mesesInicio[i]);
        // Calcula as parcelas restantes
        parcelasRestantes[i] = quantidadeParcelas[i] - mesesPassados;
        // Garante que o número de parcelas restantes não seja negativo
        if (parcelasRestantes[i] < 0) {
            parcelasRestantes[i] = 0; 
        }
    }
    return parcelasRestantes;
}

// Função para liberar a memória alocada
__declspec(dllexport) void liberarMemoria(int* ptr) {
    free(ptr);
}
