# Biblitecas necessarias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# Configuração do WebDriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
input("Aguardando login no WhatsApp Web. Pressione Enter após o login.")

# Lista de mensagens
mensagens = [
    "Olá, como vai?",
    "Tudo bem?",
    "Qual é o seu nome?",
    "Qual é a sua idade?",
    # Adicione mais mensagens aqui
]

# Lista de números de telefone para enviar mensagens
telefones = [''] # Inserir os numeros que vão receber as mensagens 

# Função para enviar mensagem
def enviar_mensagem(numero, mensagem):
    try:
        caixa_de_pesquisa = driver.find_element(By.CSS_SELECTOR, "div[title='Caixa de texto de pesquisa']")
        caixa_de_pesquisa.send_keys(numero)
        caixa_de_pesquisa.send_keys(Keys.ENTER)
        time.sleep(2)
        caixa_de_msg = driver.find_element(By.CSS_SELECTOR, "div[title='Mensagem']")
        time.sleep(1)
        caixa_de_msg.send_keys(mensagem)
        time.sleep(1)
        caixa_de_msg.send_keys(Keys.ENTER)
        time.sleep(1)
        caixa_de_pesquisa.click()
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(5)
    except Exception as e:
        print(f"Erro ao enviar mensagem para {numero}: {str(e)}")
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(5)

# Loop para enviar mensagens
while True:
    try:
        numero = random.choice(telefones)
        mensagem = random.choice(mensagens)
        enviar_mensagem(numero, mensagem)
    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário.")
        break
