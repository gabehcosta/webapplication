(function () {

    const botaoExcluir = document.querySelectorAll(".btnExcluir");

    botaoExcluir.forEach(botao => {
        botao.addEventListener("click", (e) => {
            const confirmacao = confirm("Tem certeza que quer excluir esse jogador?");
            if(!confirmacao) {
                e.preventDefault();
            }
        });
    });
})();