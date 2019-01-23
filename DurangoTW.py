#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:21:51 2018

@author: jesus
"""

import tweepy
import sqlite3
from datetime import datetime
import statistics

consumer_key = 'KEY'
consumer_secret = 'KEY'
access_token = 'KEY'
access_token_secret = 'KEY'
limite_pm25 = 20 #Limite maximo alerta
limite_pm10 = 30 #Limite maximo alerta
sqlite_file = PATH+'sensor'

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
hoy = "'"+ datetime.now().strftime("%Y-%m-%d")+"%';"
sql = "SELECT hora, pm25, pm10 FROM sensor where hora like "+hoy
c.execute(sql)
data = c.fetchall()

hora = []
pm25 = []
pm10 = []
indicehora = datetime.now()
#Medias
pm25mediah = []
pm25mediac = []
pm10mediah = []
pm10mediac = []
alertasPM25 = []
alertasPM10 = []

#Variables auxiliares
media = []
indice = 0
valormedio = 0 #Variable de almacenamiento de la media

def get_alertas(list_medias,limite):
    alertas = []
    indice = 0
    for x in list_medias:
        if x >= limite:
            alertas.append(indice)
        indice = indice + 1
    return alertas
def alertas_texto(alertasindice,alertasc,alertash):
    texto= "Hoy "
    for x in alertasindice:
        texto= texto + "a las 🚨 {}h 🚨 teniamos {}μ/m³\n".format(alertash[x].strftime('%H'),alertasc[x])
    return texto
    

for row in data:
    hora.append(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f'))#con el fin de pasar el texto a fecha
    pm25.append(row[1])
    pm10.append(row[2])
        

c.close()
conn.close()

for x in hora:
    if x.hour <= indicehora.hour:
        indicehora = x
        media.append(pm25[indice])
        indice = indice + 1
    else:
        valormedio = statistics.median(media)
        pm25mediac.append(valormedio)
        pm25mediah.append(indicehora)
        media = []
        indicehora = x
        indice= indice + 1
media = []
indice = 0       
for x in hora:
    if x.hour <= indicehora.hour:
        indicehora = x
        media.append(pm10[indice])
        indice = indice + 1
    else:
        valormedio = statistics.median(media)
        pm10mediac.append(valormedio)
        pm10mediah.append(indicehora)
        media = []
        indicehora = x
        indice= indice + 1            

alertasPM25 = get_alertas(pm25mediac,limite_pm25)
alertasPM10 = get_alertas(pm10mediac,limite_pm10)

if len(alertasPM25)>0:
    texto = "PM2.5\n" + alertas_texto(alertasPM25,pm25mediac,pm25mediah)
    api.update_status(texto)
if len(alertasPM10)>0:
    texto2 = "PM10 \n" + alertas_texto(alertasPM10,pm10mediac,pm10mediah)
    api.update_status(texto2)
