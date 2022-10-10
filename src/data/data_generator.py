# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 23:36:34 2022

@author: Luis Felipe Velasco PIA
"""
import csv, random
print("NB1300-Data")
from datetime import datetime, timedelta

cicles = input("\n Ingrese el numero de datos deseados:\n")
cicles = int(cicles)
badnumber = int(cicles*0.6)
print("Rango max falla")
print(badnumber)
badstartmax = int(cicles*0.2)
print("Rango min falla")
print(badstartmax)
badstart = random.randrange(0, badstartmax, 1)
print("Posición inicio de datos de falla")
print(badstart)

with open('NB1300.csv', 'w', newline='') as nb_file:
        writer = csv.writer(nb_file)
        writer.writerow(["Time_Stamp", "NB1300Vibracion1", "NB1300Vibracion2", "NB1300Vibracion3", "NB1300Vibracion4", "NB1300Vibracion5", "NB1300Vibracion6", "NB1300Prec", "NB1300tGener", "NB1300tCuarto", "NB1300tBloque", "NB1300tAmbien", "NB1300hCuarto", "NB1300tRuedaL", "NB1300tEscobillas", "NB1300PQA01CorrP", "NB1300pqa01VoltP" , "NB1300EstadoFalla"])
        now = datetime.now()
        for i in range(0, cicles, 1):
                td = timedelta(seconds = i)
                now1 = now + td
                if ((i >= badstart) and (i < badstart+badnumber)):
                    randnum = random.randrange(0, 100, 1)
                    if (randnum > 98):
                        writer.writerow([now1.strftime("%m/%d/%Y %H:%M:%S"), (random.randrange(31,60, 1))/10, (random.randrange(31, 60, 1))/10, (random.randrange(31, 60, 1))/10, (random.randrange(31, 60, 1))/10, (random.randrange(31, 60, 1))/10, (random.randrange(31, 60, 1))/10, (random.randrange(451, 550, 1))/10, (random.randrange(391, 440, 1))/10, (random.randrange(281, 300, 1))/10, (random.randrange(481, 560, 1))/10, (random.randrange(251, 270, 1))/10, (random.randrange(451, 550, 1))/10, (random.randrange(481, 560, 1))/10, (random.randrange(481, 560, 1))/10, (random.randrange(141, 160, 1))/10, (random.randrange(4451, 6000, 1))/10, (1)])
                    else:
                        writer.writerow([now1.strftime("%m/%d/%Y %H:%M:%S"), (random.randrange(10,30, 1))/10, (random.randrange(20, 30, 1))/10, (random.randrange(20, 30, 1))/10, (random.randrange(20, 30, 1))/10, (random.randrange(20, 30, 1))/10, (random.randrange(20, 30, 1))/10, (random.randrange(370, 450, 1))/10, (random.randrange(320, 390, 1))/10, (random.randrange(230, 280, 1))/10, (random.randrange(320, 480, 1))/10, (random.randrange(120, 250, 1))/10, (random.randrange(220, 450, 1))/10, (random.randrange(320, 480, 1))/10, (random.randrange(320, 480, 1))/10, (random.randrange(120, 140, 1))/10, (random.randrange(4350, 4450, 1))/10, (0)])
                else:
                    writer.writerow([now1.strftime("%m/%d/%Y %H:%M:%S"), (random.randrange(10,30, 1))/10, (random.randrange(20, 30, 1))/10, (random.randrange(20, 30, 1))/10, (random.randrange(20, 30, 1))/10, (random.randrange(20, 30, 1))/10, (random.randrange(20, 30, 1))/10, (random.randrange(370, 450, 1))/10, (random.randrange(320, 390, 1))/10, (random.randrange(230, 280, 1))/10, (random.randrange(320, 480, 1))/10, (random.randrange(120, 250, 1))/10, (random.randrange(220, 450, 1))/10, (random.randrange(320, 480, 1))/10, (random.randrange(320, 480, 1))/10, (random.randrange(120, 140, 1))/10, (random.randrange(4350, 4450, 1))/10, (0)])
