from itertools import count
from operator import index
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
#from twitter_scraper_selenium import scrap_profile Remover dps
from twitter_scraper_selenium import scrap_keyword
from bs4 import BeautifulSoup
import math

def verificadup(temp, dado):
    lista = temp
    valor = dado
    resultado = False
    for i in range(len(lista)):
        if lista[i] == valor:
            resultado = True
    return resultado

def computeTF(wordDict, bow): 
    tfDict = {}
    total = len(wordDict)
    
    #for word in wordDict:
    count = wordDict.count(bow)
    tfDict[bow] = count/ float(total)
    with open("tf.txt", "a") as f:
        f.write(str(indice) + ":" + str(bow) + ":" + str(tfDict[bow]) + "\n")
    
    return tfDict

def computeIDF(wordDict, bow):
    idfDict = {}
    N = len(wordDict)
    val = []
    for fras in temp:
        pal = fras.split()
        for b in pal:
            val.append(b)
    tam = val.count(bow)
    idfDict[bow] = math.log10(N / (float(tam) + 1))
    with open("idf.txt", "a") as f:
        f.write(str(indice) + ":" + str(bow) + ":" + str(idfDict[bow]) + "\n")
        
    return(idfDict)

def computeTFIDF(wordDict, bow):
    tfDict = {}
    total = len(wordDict)
    
    #for word in wordDict:
    count = wordDict.count(bow)
    tfDict[bow] = count/ float(total)

    idfDict = {}
    N = len(wordDict)
    val = []
    for fras in temp:
        pal = fras.split()
        for b in pal:
            val.append(b)
    tam = val.count(bow)
    idfDict[bow] = math.log10(N / (float(tam) + 1))


    tfidf = {}


    tfidf[bow] = tfDict[bow]*idfDict[bow]
    with open("tf_idf.txt", "a") as f:
        f.write(str(indice) + ":" + str(bow) + ":" + str(tfidf[bow]) + "\n")
    return(tfidf)


exe_path = GeckoDriverManager().install()
service=Service(exe_path)
browser = webdriver.Firefox(service=service)

# Esconde o navegador


usuario = "FaesaTwiter"
senha = "Howard4@"

browser.get("https://twitter.com/login")
print("Acessou o Twitter...")
sleep(3)

try:
    campo_nome_usuario = browser.find_element(by=By.XPATH, value="//input[contains(@name,'text')]")    
    campo_nome_usuario.click()
    campo_nome_usuario.send_keys(usuario)
    campo_nome_usuario.send_keys(Keys.RETURN)
    print("Entrou com o nome de usuário...")
    sleep(2)
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    browser.quit()
    exit(1)

try:
    campo_senha = browser.find_element(by=By.XPATH, value="//input[contains(@name,'password')]")    
    # campo_senha.click()
    campo_senha.send_keys(senha)
    campo_senha.send_keys(Keys.RETURN)
    print("Entrou com a senha de usuário...")
    sleep(1)
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    browser.quit()
    exit(1)

sleep(3)


temp = ["teste"]
indice = 0
while (True):
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
 
    content_principal = soup.find("div", attrs={"class": "css-1dbjc4n"})

    extracted_data = {}

    names_principal = content_principal.find_all("div", attrs={"data-testid": "tweetText"})
  
    for e in names_principal:
        dado = e.get_text()
        
        if verificadup(temp, dado) == False:
            with open("tweets.txt", "a") as f:
                indice +=1
                f.write(str(indice) + ":" + dado + ";" +"\n")
                temp.append(dado)
                frases = dado.split()
                for palavra in frases:
                    computeTF(frases, palavra)
                    computeIDF(frases, palavra)
                    computeTFIDF(frases, palavra)

    
    browser.refresh()
    sleep(30)


