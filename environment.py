from browser import Browser
from multiprocessing import context

#Executar antes de rodar todos os testes
def before_all(context):
    context.browser = Browser()

#Executar depois que todos os testes acabarem
def after_all(context):
    context.browser.fechar_browser()

#Executar depois que rodar cada cenário
def after_scenario(context, scenario):
    context.browser.limpar_browser()