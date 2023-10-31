from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

class ComponentesEcommerce(object):
    input_user = '[id = "user-name"]'
    input_password = '[id = "password"]'
    botao_logar = '[id = "login-button"]'
    pesquisa = '[class = "product_sort_container"]'
    pesquisa_selecao = '[class = "product_sort_container"]'
    produto_selecao = '[id = "item_5_title_link"]'
    botao_adicionar = '[id = "add-to-cart-sauce-labs-fleece-jacket"]'
    botao_carrinho = '[id = "shopping_cart_container"]'
    preco_carrinho = '[class = "inventory_item_price"]'
    botao_checkout = '[id = "checkout"]'
    input_nome = '[id = "first-name"]'
    input_sobrenome = '[id = "last-name"]'
    input_caixa_postal = '[id = "postal-code"]'
    botao_continuar = '[id = "continue"]'
    botao_finalizar = '[id = "finish"]'
    texto_final = '[class = "complete-header"]'

class EcommerceResultados():
    def __init__(self, driver):
        self.driver = driver 

    def pegar_elemento(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def acessar_pagina(self, link):
        self.driver.get(link)

    def clicar_logar(self):
        element = self.pegar_elemento(ComponentesEcommerce.botao_logar)
        WebDriverWait(self.driver, 10).until(ec.visibility_of(element))
        element.click()
    
    def logar(self, user, password):
        self.pegar_elemento(ComponentesEcommerce.input_user).send_keys(user)
        self.pegar_elemento(ComponentesEcommerce.input_password).send_keys(password)
        self.clicar_logar()

    def pesquisar(self):
        elemento_selecao = self.pegar_elemento(ComponentesEcommerce.pesquisa_selecao)
        select = Select(elemento_selecao)
        select.select_by_visible_text('Price (high to low)')

    def selecionar_produto(self):
        self.pegar_elemento(ComponentesEcommerce.produto_selecao).click()
       
    def adicionar_carrinho(self):
        time.sleep(2)
        self.pegar_elemento(ComponentesEcommerce.botao_adicionar).click()
    
    def acessar_carrinho(self):
        self.pegar_elemento(ComponentesEcommerce.botao_carrinho).click()

    def validar_carrinho(self):
        total = self.pegar_elemento(ComponentesEcommerce.preco_carrinho).text
        assert total == '$49.99'
    
    def finalizar_carrinho(self):
        time.sleep(2)
        self.pegar_elemento(ComponentesEcommerce.botao_checkout).click()

    def inserir_dados(self, nome, sobrenome, caixa_postal):
        self.pegar_elemento(ComponentesEcommerce.input_nome).send_keys(nome)
        self.pegar_elemento(ComponentesEcommerce.input_sobrenome).send_keys(sobrenome)
        self.pegar_elemento(ComponentesEcommerce.input_caixa_postal).send_keys(caixa_postal)
        self.pegar_elemento(ComponentesEcommerce.botao_continuar).click()

    def finalizar_compra(self):
        self.pegar_elemento(ComponentesEcommerce.botao_finalizar).click()

    def validar_compra(self):
        self.pegar_elemento(ComponentesEcommerce.texto_final) == 'Thank you for your order!'

    def historico(self):
        self.acessar_carrinho()



       
