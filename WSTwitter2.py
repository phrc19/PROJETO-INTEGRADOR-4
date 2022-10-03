from time import sleep

from twitter_scraper_selenium import scrap_keyword
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
    
    with open('tweets3.txt', "a") as f:
        for i in temp:
            f.write(str(i) + ";")

        print('Aguardando próximo processamento')
        
        sleep(3600)
