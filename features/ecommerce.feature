#language: pt

Funcionalidade: fazer uma compra no saucedemo

Contexto: acessar a página para o teste
    Dado que acesso a página da saucedemo

Cenário: acessar a página da saucedemo
    Dado que eu estiver logado no site
    Quando efetuar uma pesquisa no site (selecionando ordenação dos produtos)
    Então devo selecionar o produto
    Então devo clicar no botão de Adicionar ao carrinho
    Então devo clicar no carrinho
    Então devo verificar se o preço total está correto
    Então devo fechar o pedido no botão de checkout
    Então devo inserir credenciais
    Então devo devo finalizar minha compra
    Então devo validar o sucesso da compra
    Então devo verificar o histórico de pedido