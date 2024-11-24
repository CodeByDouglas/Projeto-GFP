
const staticBaseUrl = "/static/"; // Caminho base para arquivos estáticos
const infoContent = {
    1: {
        title: "Módulo 1: Introdução ao GFP",
        description: "- A gestão financeira é fundamental para manter o equilíbrio entre receitas e despesas, permitindo que indivíduos ou empresas alcancem seus objetivos financeiros em diferentes horizontes de tempo. Envolve planejamento, organização e controle eficiente dos recursos financeiros. A boa gestão permite evitar dívidas excessivas, criar reservas de emergência, investir para o futuro e aumentar a segurança financeira, o que resulta em mais tranquilidade e controle sobre o próprio dinheiro.",
        tutorial: {
            intro: "Aprenda como utilizar as principais páginas do site para organizar suas finanças.",
            pages: [
                {name: "Menu lateral",
                 steps: [
                    {
                        text: "Menu de aceso para as outras páginas do site:",
                        image: `${staticBaseUrl}image/MENU.png`
                    }
                 ]
                },
                {
                    name: "Dashboard",
                    steps: [
                        {
                            text: "1. Acesse o Dashboard para uma visão geral do seu status financeiro, incluindo receitas, despesas e saldo atual:",
                            image: `${staticBaseUrl}image/DASHBOARD.png`
                        }
            ]},
                
                 {   name: "Perfil",
                    steps: [
                        {
                            text: "1. Acesse o Perfil para atualizar suas informações pessoais, como nome, senha e rendas:",
                            image: `${staticBaseUrl}image/PERFIL.png`
                        }
                    ]
                 },
                {
                    name: "Extrato de Despesas",
                    steps: [
                        {
                            text: "1. No Extrato de Despesas, visualize todas as suas transações organizadas por data:",
                            image: `${staticBaseUrl}image/EXTRATO.png`
                        },
                    ]
                },
                {
                    name: "Lançamento de Despesas",
                    steps: [
                        {
                            text: "<b>Ocasional</b>: Adicione despesas que não apresentam uma recorrência fixa, que de fato acontecem ocasionalmente durante o mês:",
                            image: `${staticBaseUrl}image/DESP AVULSA.png`
                        },
                        {
                            text: "<b>Fixa</b>: Adicione despesas que se repetem durante todos os meses. Adicione uma data para a fizalização.Ex: data anual:",
                            image: `${staticBaseUrl}image/DESP FIXAS.png`
                        },
                        {
                            text: "<b>Parcelada</b>: Adicione despesas divididas em prestações, sendo elas despesas que não são pagas no valor total de uma só vez:",
                            image: `${staticBaseUrl}image/DESP FIXAS-1.png`
                        }
                    ]
                }
            ]
        },
        dica: "Dica: Explore mais conteúdos no site para aprender técnicas de gestão financeira e manter suas finanças sob controle!"
    },
    2: {
        title: "Módulo 2: Fundamentos de Finanças Pessoais",
        description: `- Conceitos fundamentais para entender e gerir suas finanças de forma eficaz:
        <div style="margin-left: 20px">
            Receita: Refere-se a todo o dinheiro que uma pessoa recebe, incluindo salário, aluguéis, rendimentos de investimentos ou outras fontes.
            Despesa: São os gastos ou saídas de dinheiro para cobrir necessidades e desejos, como contas mensais, alimentação, transporte e lazer.
            Ativos: Bens ou investimentos que geram renda ou aumentam o patrimônio, como imóveis, ações e investimentos em poupança.
            Passivos: Obrigações financeiras ou dívidas que demandam pagamento, incluindo empréstimos, financiamentos e cartões de crédito. Saber distinguir entre ativos e passivos é essencial para construir riqueza de forma sólida e sustentável.</div>`,
        dica: "Dica: Aprenda a criar um orçamento pessoal e a controlar suas despesas para melhorar sua saúde financeira."
    },
    3: {
        title: "Módulo 3: Planejamento Financeiro",
        description: "- O planejamento financeiro permite estabelecer e alcançar objetivos de curto, médio e longo prazo. Ele envolve a criação de um orçamento para monitorar receitas e despesas, definir metas claras e avaliar regularmente o progresso. A organização dos recursos é a chave para transformar sonhos em realidade, seja economizando para uma emergência, seja investindo para o futuro.",
        dica: "Dica: Confira os guias práticos de planejamento financeiro no site para ajudá-lo a organizar suas metas e manter o foco!"
    },
    4: {
        title: "Módulo 4: Gestão de Dívidas",
        description: `A gestão de dívidas é vital para alcançar estabilidade financeira, sendo necessário escolher um método adequado para pagá-las.<br>
        <div style="margin-left: 20px">
         -Bola de Neve: Priorize o pagamento das menores dívidas primeiro. Esse método oferece ganhos psicológicos ao eliminar dívidas mais rapidamente, o que pode motivar a continuidade do processo;<br>
         -Avalanche: Foca em quitar primeiro as dívidas com as maiores taxas de juros, economizando em juros ao longo do tempo. Esse método é financeiramente mais vantajoso;<br>
         -Planejamento e Controle: Análise e redução de taxas de juros, renegociação de prazos e prorrogações quando possível para aliviar o fluxo de caixa.
         </div>`,
        dica: "Dica: Aprenda mais sobre as estratégias de quitação de dívidas em nossos artigos e escolha o método que melhor se adapta à sua situação!"
    },
    5: {
        title: "Módulo 5: Poupança e Investimentos",
        description: `<b>Comparação entre poupança e investimento para diferentes objetivos e prazos.</b><br>
          <div style="margin-left: 20px">
            -Poupança: Ideal para objetivos de curto prazo ou para a construção de uma reserva de emergência. Oferece segurança e liquidez, mas com retornos limitados.<br>
            -Investimentos: Para metas de médio e longo prazo, os investimentos apresentam potencial de rendimento superior, mas exigem tolerância ao risco. As opções variam de renda fixa (CDBs, Tesouro Direto) a renda variável (ações, fundos de investimentos), com o objetivo de preservar e expandir o poder de compra ao longo do tempo.
        </div>
        <b>Escolha Conforme a Necessidade:</b><br>
        <div style="margin-left: 20px">
        - Curto Prazo e Emergências: A poupança é preferível pela acessibilidade imediata.<br>
       - Médio e Longo Prazo: Investimentos diversificados e planejados ajudam a construir um patrimônio que pode superar a inflação e gerar crescimento real.
        </div>`,

       
        dica: "Dica: Veja no site análises comparativas entre poupança e diferentes tipos de investimentos para tomar decisões informadas!"
    },
    6:{
        title:"Módulo 6: Objetivos de longo prazo",
        description:"- Os objetivos de longo prazo demandam de 5 a 20 anos ou mais para serem realizados e incluem metas como aposentadoria, aquisição de imóveis, e independência financeira. A criação de um plano estruturado, aliada à disciplina, é essencial para acumular recursos de forma consistente. Revisões periódicas dos objetivos e do plano ajudam a manter o foco e realizar ajustes conforme as circunstâncias mudam.",
        dica:"Dica: Acesse conteúdos específicos sobre planejamento de longo prazo no site e comece a definir suas metas agora!"

    },
    7:{
        title:"Módulo 7: Mentalidade financeira",
        description:"- Ter controle emocional e cultivar bons hábitos financeiros é essencial para alcançar uma mentalidade financeira equilibrada. Isso inclui resistir ao consumismo impulsivo, desenvolver a paciência necessária para economizar e investir no longo prazo, e entender que o bem-estar financeiro vai além do dinheiro, impactando a qualidade de vida. Educação financeira e disciplina pessoal são fatores que, juntos, constroem uma mentalidade orientada ao sucesso financeiro.",
        dica:"Dica: No site, você encontra dicas de especialistas para desenvolver hábitos financeiros mais saudáveis e melhorar seu controle emocional!"

    },
    8:{
        title:"Módulo 8: Orçamento de controle de gastos",
        description:"- Um orçamento é a ferramenta prática que permite o controle financeiro. Inclui monitorar despesas fixas e variáveis, analisar categorias de gastos e definir limites para cada uma delas. Ferramentas digitais como aplicativos de finanças podem facilitar o acompanhamento. O objetivo é ter clareza sobre para onde o dinheiro vai e identificar onde é possível economizar para priorizar metas financeiras.",
        dica:"Dica: Aproveite nossas planilhas no site para organizar seu orçamento e otimizar seus gastos!"

    },
    9:{
        title:"Módulo 9: Educação financeira e autocontrole",
        description:"- A educação financeira contínua é essencial para o sucesso na gestão financeira pessoal. Incentive a busca por livros, cursos, e até mesmo palestras sobre finanças. Além disso, é importante o desenvolvimento de autocontrole para resistir a compras impulsivas e evitar o endividamento. Aprender sobre finanças promove decisões mais informadas e uma vida financeira mais equilibrada.",
        dica:"Dica: Visite a seção de educação financeira no site para acessar uma variedade de recursos que ajudam a melhorar seu conhecimento e autocontrole!"

    },
    10:{
        title:"Módulo 10: Proteção financeira e seguro",
        description:"- Além de poupança e investimentos, ter seguros (como de saúde, vida, carro e residência) pode proteger contra imprevistos significativos. Esses produtos financeiros ajudam a minimizar perdas em caso de eventos inesperados, garantindo uma segurança adicional para você e sua família, permitindo uma continuidade no planejamento financeiro sem grandes interrupções.",
        dica:"Dica: Consulte nossos artigos para entender como diferentes tipos de seguros podem proteger seu patrimônio e garantir sua tranquilidade financeira!"
                
    },
    11:{
        title:"Módulo 11: Diversificação de investimentos",
        description:"- A diversificação, ou a distribuição do dinheiro em diferentes tipos de investimento, é uma forma de reduzir riscos e aumentar potencial de retorno. Investir em uma variedade de ativos ajuda a proteger o portfólio contra perdas em situações adversas de mercado, aumentando as chances de bons retornos ao longo do tempo e promovendo uma maior segurança no crescimento do patrimônio.",
        dica:"Dica: Aprenda estratégias de diversificação em nossos artigos para melhorar seu portfólio de investimentos!"
    }
    // Adicione mais módulos conforme necessário
};

function showInfo(step) {
    const infoBox = document.getElementById("info-box");

    const content = infoContent[step];
    if (!content) {
        infoBox.innerHTML = "<p>Informações não disponíveis para este módulo.</p>";
        return;
    }

    const title = content.title ? `<h3>${content.title}</h3>` : '';
    const description = content.description ? `<p>${content.description}</p>` : '';
    const dica = content.dica ? `<p>${content.dica}</p>` : '';

    let itemsHTML = '';
    if (content.items) {
        itemsHTML = '<ul>';
        content.items.forEach(item => {
            itemsHTML += `<li>${item}</li>`;
        });
        itemsHTML += '</ul>';
    }

    let tutorialHTML = '';
    if (content.tutorial) {
        tutorialHTML += `<h4>Tutorial</h4>`;
        tutorialHTML += `<p>${content.tutorial.intro}</p>`;
        content.tutorial.pages.forEach(page => {
            tutorialHTML += `<h5>${page.name}</h5>`;
            page.steps.forEach(step => {
                tutorialHTML += `
                    <div style="margin-bottom: 20px;">
                        <p>${step.text}</p>
                        <img 
                            src="${step.image}" 
                            alt="${page.name} Tutorial Step" 
                            style="width: 100%; max-width: 400px; height: auto; display: block; margin: 20px auto; cursor: pointer;"
                            onclick="openPopup('${step.image}')">
                    </div>
                `;
            });
        });
    }

    infoBox.innerHTML = `
        ${title}
        ${description}
        ${itemsHTML}
        ${tutorialHTML}
        ${dica}
    `;
}

function openPopup(imageSrc) {
    const popup = document.getElementById("image-popup");
    const popupImg = document.getElementById("popup-img");

    // Define o caminho da imagem no popup
    popupImg.src = imageSrc;

    // Exibe o popup
    popup.style.display = "flex";
}

function closePopup() {
    const popup = document.getElementById("image-popup");

    // Oculta o popup
    popup.style.display = "none";
}
