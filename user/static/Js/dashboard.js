document.addEventListener('DOMContentLoaded', function() {
    var ctxCategorias = document.getElementById('graficoCategorias').getContext('2d');
    var graficoCategorias = new Chart(ctxCategorias, {
        type: 'bar',
        data: {
            labels: JSON.parse(document.getElementById('categorias_json').textContent), // Array de rótulos
            datasets: [{
                label: 'Despesas por Categoria',
                data: JSON.parse(document.getElementById('valores_json').textContent), // Array de valores
                backgroundColor: 'rgba(25, 135, 84, 0.5)', // Cor verde com transparência
                borderColor: 'rgba(25, 135, 84, 1)', // Cor verde sem transparência
                borderWidth: 1
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: false // Desativa a legenda para remover o botão de filtro
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    var ctxPorcentagens = document.getElementById('graficoPorcentagens').getContext('2d');
    var graficoPorcentagens = new Chart(ctxPorcentagens, {
        type: 'doughnut',
        data: {
            labels: JSON.parse(document.getElementById('categorias_porcentagem_json').textContent), // Array de rótulos
            datasets: [{
                label: 'Porcentagem de Despesas por Categoria',
                data: JSON.parse(document.getElementById('porcentagens_json').textContent), // Array de valores
                backgroundColor: [
                    'rgba(255, 99, 132, 0.5)',
                    'rgba(54, 162, 235, 0.5)',
                    'rgba(255, 206, 86, 0.5)',
                    'rgba(75, 192, 192, 0.5)',
                    'rgba(153, 102, 255, 0.5)',
                    'rgba(255, 159, 64, 0.5)',
                    'rgba(199, 199, 199, 0.5)',
                    'rgba(83, 102, 255, 0.5)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(199, 199, 199, 1)',
                    'rgba(83, 102, 255, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'left', // Posiciona a legenda acima do gráfico
                    labels: {
                        color: '#182933' // Define a cor do texto da legenda para garantir visibilidade
                    }
                }
            }
        }
    });
});