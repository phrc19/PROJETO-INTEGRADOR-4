from importlib.resources import contents
from itertools import count
from operator import index
from os import sep


from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from twitter_scraper_selenium import scrap_profile 
from twitter_scraper_selenium import scrap_keyword
import pandas as pd
import csv

temp = []
while(True):
    chaves = ['bolsonaro','lula','ciro gomes','simone tebet','felipe davila','leo pericles','roberto jefferson', 'vera lucia', 'pablo marçal', 'soraya thronicke', 'sofia manzano']
    for i in chaves:

        scrap_keyword(keyword= i, browser="firefox",tweets_count=50,output_format="csv", filename="tweets")

        tweet = open('tweets.csv', encoding='utf-8')
        linhas = csv.reader(tweet)
        

        for linha in linhas:
            if linha[9] != "content":
                temp.append(linha[9])
    
    with open('tweets2.txt', "a") as f:
        for i in temp:
            f.write(str(i) + "\n")

        print('Aguardando próximo processamento')
        
        sleep(3600)