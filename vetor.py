from itertools import count
from operator import index
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


import math
import pandas as pd
import math 



def computeTF(wordDict, doc):
    tfDict = {}
    corpusCount = len(doc)
    for word, count in wordDict.items():
        tfDict[word] = count/float(corpusCount)
    return(tfDict)
    

def computeIDF(docList):
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0) 
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / (float(val) + 1))
        
    return(idfDict)

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return(tfidf)

def computeIDFF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        if val == 0:
            tfidf[word] = 0
        else:
            tfidf[word] = idfs[word]
    return(tfidf)

#Nosso web scrapping retornou 35k de arquivos, por isso geramos um arquivo menor nomeado tw.txt

arq = open("tw.txt")
linhas = arq.readlines()

listaContagemDicionario = []
tfWordDict = []
idfWordDict = []
total = []
tfidf = []
idf = []
for linha in linhas:
    fras_sep = linha.split()
    total = set(total).union(set(fras_sep))

for linha in linhas:
    frase_separada = linha.split()
    wordDict = dict.fromkeys(total, 0)
    for word in frase_separada:
        wordDict[word]+=1
    tfWordDict.append(computeTF(wordDict, linha))
    listaContagemDicionario.append(wordDict)
    #idfWordDict.append(computeIDF(wordDict))

tf = pd.DataFrame(tfWordDict)
tf.to_csv("tf.csv")
idfs = computeIDF(listaContagemDicionario)

for tf in tfWordDict:
    tfidf.append(computeTFIDF(tf, idfs))
    idf.append(computeIDFF(tf, idfs))
idftf = pd.DataFrame(tfidf)
idftf.to_csv("idftf.csv")
idff = pd.DataFrame(idf)
idff.to_csv("idf.csv")
