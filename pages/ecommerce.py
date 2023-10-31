from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

class ComponentesEcommerce(object):
    input_user = '[id = "user-name"]'
    input_password = '[id = "password"]'
    botao_logar = '[id = "login-button"]'
    pesquisa = '[class = "product_sort_container"]'
    pesquisa_selecao = '[class = "product_sort_container"]'
    produto_selecao = '[id = "item_5_title_link"]'

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
        self.pegar_elemento(ComponentesEcommerce.pesquisa).submit()

    def selecionar_produto(self):
        element = self.pegar_elemento(ComponentesEcommerce.produto_selecao)
        WebDriverWait(self.driver, 30).until(ec.visibility_of(element))
        element.click()
        

       
