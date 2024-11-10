const infoContent = {
    1: {
        title: "Módulo 1: Introdução ao GFP",
        description: "A gestão financeira é fundamental para manter o equilíbrio entre receitas e despesas, permitindo que indivíduos ou empresas alcancem seus objetivos financeiros em diferentes horizontes de tempo. Envolve planejamento, organização e controle eficiente dos recursos financeiros. A boa gestão permite evitar dívidas excessivas, criar reservas de emergência, investir para o futuro e aumentar a segurança financeira, o que resulta em mais tranquilidade e controle sobre o próprio dinheiro.",
        dica: "Explore mais conteúdos no site para aprender técnicas de gestão financeira e manter suas finanças sob controle!"
    },
    2: {
        title: "Módulo 2: Fundamentos de Finanças Pessoais",
        description: "As finanças pessoais envolvem a gestão do dinheiro de um indivíduo ou família, incluindo receitas, despesas, investimentos e planejamento financeiro. É essencial para garantir a segurança financeira e alcançar objetivos de curto, médio e longo prazo.",
        dica: "Aprenda a criar um orçamento pessoal e a controlar suas despesas para melhorar sua saúde financeira."
    },
    // Adicione mais módulos conforme necessário
};

function showInfo(step) {
    const infoBox = document.getElementById("info-box");
    infoBox.innerHTML = `
        <h3>${infoContent[step].title}</h3>
        <p>${infoContent[step].description}</p>
        <p>${infoContent[step].dica}</p>
    `;
}