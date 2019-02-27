
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:18:25 2018
@author: jesus
"""
import matplotlib
matplotlib.use('Agg')
import sqlite3,statistics,os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


PATH=os.path.dirname(os.path.abspath(__file__))
sqlite_file = PATH+'/sensor.sql' #Datos recogidos por el sensor

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

ahora = datetime.now().strftime("%Y-%m-%d")
hoy = "'"+ahora+"%';"

sql = "SELECT hora, aqi FROM data where hora like "+hoy
c.execute(sql)
data = c.fetchall()

hora = []
aqi = []

for row in data:
    hora.append(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f'))#con el fin de pasar el texto a fecha
    aqi.append(row[1])
        

c.close()
conn.close()

indicehora = datetime.now()
aqihora = []
aqimediah = []
aqimediac = []
media = []
indice = 0
valormedio = 0
for x in hora:
    if x.hour <= indicehora.hour:
        indicehora = x
        media.append(aqi[indice])
        indice = indice + 1
    else:
        valormedio = statistics.median(media)
        aqimediac.append(valormedio)
        aqimediah.append(indicehora)
        media = []
        indicehora = x
        indice= indice + 1
media = []
indice = 0       

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("AQI EPA\nDurango "+ahora)

   # Configure x-ticks
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

   # Plot temperature data on left Y axis
ax1.set_ylabel("AQI")
ax1.plot_date(hora, aqi, '-', label="AQI>20 Peligro", color='g')
ax1.plot_date(aqimediah, aqimediac,'-', label="AQI Media", color='g')

   

   # Format the x-axis for dates (label formatting, rotation)
fig.autofmt_xdate(rotation=60)
#fig.tight_layout()

   # Show grids and legends
ax1.grid(True)
ax1.legend(loc='best', framealpha=0.5)


plt.savefig(PATH+"/figure.png")
