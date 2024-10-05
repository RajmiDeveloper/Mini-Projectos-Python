import tkinter as tk
import pymysql as ps


conect = ps.connect(host='190.7.56.92', user='fotok0_visitor',passwd = 'VisitanteQueLlegaDesdeLaLuna', db='fotok0_dokkan_calculator')
cur = conect.cursor()

cur.execute('SELECT * from character_info')

for bd in cur:
    print(bd)

conect.close()

