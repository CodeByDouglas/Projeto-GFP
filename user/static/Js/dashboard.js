document.addEventListener('DOMContentLoaded', function() {
    const windows = document.querySelectorAll('.window');
    
    windows.forEach(window => {
        window.addEventListener('click', function() {
            alert(`Você clicou na janela: ${this.querySelector('.window-title').innerText}`);
        });
    });

    // Dados do gráfico de barras
    const categorias = JSON.parse(document.getElementById('categorias_json').textContent);
    const valores = JSON.parse(document.getElementById('valores_json').textContent);

    // Configuração do gráfico de barras
    const ctxBar = document.getElementById('barChart').getContext('2d');
    const barChart = new Chart(ctxBar, {
        type: 'bar',
        data: {
            labels: categorias,
            datasets: [{
                label: 'Valores',
                data: valores,
                backgroundColor: 'rgba(25, 135, 84, 0.6)', // Cor verde com transparência mais forte
                borderColor: 'rgba(25, 135, 84, 1)', // Cor verde sem transparência
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false // Desativa a exibição da legenda
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        color: '#182933' // Cor dos valores no eixo Y
                    }
                },
                x: {
                    ticks: {
                        color: '#182933' // Cor das palavras da categoria no eixo X
                    }
                }
            }
        }
    });

    // Dados do gráfico de rosca
    const categoriasPorcentagem = JSON.parse(document.getElementById('categorias_porcentagem_json').textContent);
    const porcentagens = JSON.parse(document.getElementById('porcentagens_json').textContent);

    // Configuração do gráfico de rosca
    const ctxDoughnut = document.getElementById('doughnutChart').getContext('2d');
    const doughnutChart = new Chart(ctxDoughnut, {
        type: 'doughnut',
        data: {
            labels: categoriasPorcentagem,
            datasets: [{
                label: 'Porcentagens',
                data: porcentagens,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.6)', // Cor mais forte
                    'rgba(54, 162, 235, 0.6)', // Cor mais forte
                    'rgba(255, 206, 86, 0.6)', // Cor mais forte
                    'rgba(75, 192, 192, 0.6)', // Cor mais forte
                    'rgba(153, 102, 255, 0.6)', // Cor mais forte
                    'rgba(255, 159, 64, 0.6)' // Cor mais forte
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: true, // Exibe a legenda
                    position: 'right', // Alinha a legenda à direita
                    labels: {
                        boxWidth: 20, // Largura da caixa de cor da legenda
                        padding: 20, // Espaçamento entre os itens da legenda
                        font: {
                            size: 16, // Aumenta o tamanho da fonte das legendas
                            family: 'Montserrat', // Define a família da fonte
                            weight: 'bold', // Define o peso da fonte
                            color: '#182933' // Define a cor da fonte
                        },
                        usePointStyle: true, // Usa ícones de ponto para a legenda
                        pointStyle: 'rectRounded', // Define o estilo do ponto como retângulo arredondado
                        borderRadius: 5, // Adiciona borda arredondada ao ícone de categoria
                        borderWidth: 2, // Define a largura da borda do ícone de categoria
                        borderColor: '#182933' // Define a cor da borda do ícone de categoria
                    }
                }
            },
            layout: {
                padding: {
                    left: 10,
                    right: 10,
                    top: 10,
                    bottom: 10
                }
            }
        }
    });
});