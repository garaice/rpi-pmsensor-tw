#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Copyright 2017 Dr. M. Luetzelberger <webmaster@raspberryblog.de>
#  https://github.com/luetzel
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sqlite3,time,os
import datetime
from sds011 import SDS011

PATH=os.path.dirname(os.path.abspath(__file__))

sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
conn = sqlite3.connect(PATH+'/sensor') #Conexion a SQLite3

punterodb = conn.cursor()
fecha = datetime.datetime.now()




def savePM(pm):
    sql= "INSERT INTO datos VALUES ('{}',{},{});".format(str(fecha),str(pm[0]),str(pm[1]))
    print(sql)
    punterodb.execute(sql)
    conn.commit()


def main(args):
    sensor.sleep(sleep=False)
    time.sleep(15)
    pm = sensor.query()
    time.sleep(5)
    sensor.sleep()
    savePM(pm)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
