from behave import * 
# from nose.tools import *
from pages.ecommerce import *

componentesEcommerce = ComponentesEcommerce()
ecommerceResultados = EcommerceResultados(driver)

@given(u'que acesso a página da saucedemo')
def step_impl(context):
    ecommerceResultados.acessar_pagina('https://www.saucedemo.com/')


@given(u'que eu estiver logado no site')
def step_impl(context):
    ecommerceResultados.logar('standard_user', 'secret_sauce')


@when(u'efetuar uma pesquisa no site (selecionando ordenação dos produtos)')
def step_impl(context):
    ecommerceResultados.pesquisar()


@then(u'devo selecionar o produto')
def step_impl(context):
    ecommerceResultados.selecionar_produto()

@then(u'devo clicar no botão de Adicionar ao carrinho')
def step_impl(context):
    ecommerceResultados.adicionar_carrinho()


@then(u'devo clicar no carrinho')
def step_impl(context):
    ecommerceResultados.acessar_carrinho()

@then(u'devo verificar se o preço total está correto')
def step_impl(context):
    ecommerceResultados.validar_carrinho()


@then(u'devo fechar o pedido no botão de checkout')
def step_impl(context):
    ecommerceResultados.finalizar_carrinho()


@then(u'devo inserir credenciais')
def step_impl(context):
    ecommerceResultados.inserir_dados('Teste', 'Teste', '12345')


@then(u'devo devo finalizar minha compra')
def step_impl(context):
    ecommerceResultados.finalizar_compra()

@then(u'devo validar o sucesso da compra')
def step_impl(context):
    ecommerceResultados.validar_compra()

@then(u'devo verificar o histórico de pedido')
def step_impl(context):
    ecommerceResultados.historico()
