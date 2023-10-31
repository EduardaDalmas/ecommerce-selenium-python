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


# @then(u'devo clicar no botão de Adicionar ao carrinho')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then devo clicar no botão de Adicionar ao carrinho')


# @then(u'devo clicar no carrinho')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then devo clicar no carrinho')


# @then(u'devo verificar se o produto foi adicionado corretamente ao carrinho')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then devo verificar se o produto foi adicionado corretamente ao carrinho')


# @then(u'devo verificar se o preço total está correto')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then devo verificar se o preço total está correto')


# @then(u'devo fechar o pedido no botão de checkout')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then devo fechar o pedido no botão de checkout')


# @then(u'devo inserir meu nome')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then devo inserir meu nome')


# @then(u'devo inserir meu sobrenome')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then devo inserir meu sobrenome')


# @then(u'devo inserir meu codigo postal')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then devo inserir meu codigo postal')


# @then(u'devo devo finalizar minha compra')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then devo devo finalizar minha compra')


# @then(u'devo verificar o histórico de pedido')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then devo verificar o histórico de pedido')