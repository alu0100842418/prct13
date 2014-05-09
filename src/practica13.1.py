#!/usr/bin/python
#!encoding: UTF-8

import modulo.py
import pylab as dibujo

x=[]
for i in x:
  ti = clock()
  error(i, , )
  tf = clock
  y =tf-ti
  Y = Y + [y]

#x1 = [1,2,3,4,5]
#x2 = [10,50,100,150,500,550,1000]
#y1 = [20,90,100,98,98]
#y2 = [0,10,50,98,98]
#y3 = [0,0,20,90,98]
#y4 = [0,0,10,60,98]
#y5 = [0,0,0,10,50]
#y6 = [0,0,0,0,20]
#y7 = [0.0,0.0,0.03,0.02,0.15,0.15,0.2]

p1 = dibujo.subplot(211) #2 = Dos filas, 1 = Una columna, 1 = Primer dibujo

dibujo.plot (x1,y1, marker='o', linestyle='-', color='r', label='10')
dibujo.plot (x1,y2, marker='', linestyle='-', color='b', label='50')
dibujo.plot (x1,y3, marker='o', linestyle=':', color='g', label='100')
dibujo.plot (x1,y4, marker='*', linestyle=':', color='c', label='150')
dibujo.plot (x1,y5, marker='*', linestyle='--', color='m', label='500')
dibujo.plot (x1,y6, marker='s', linestyle='-.', color='y', label='1000')

dibujo.title ('Porcentajes de error')

dibujo.legend()

dibujo.xlim(0, 7) #Cambia la escala del dibujo
dibujo.ylim(-20,120)
dibujo.xticks(x1) #x va entre paréntesis porque es la que quiero que me visualice

p2 = dibujo.subplot(212)
dibujo.plot (x2,y7, linestyle='-', color='r')

dibujo.xlabel ('Intervalos')
dibujo.ylabel ('Tiempo en segundos')

dibujo.xlim(0, 1100) #Cambia la escala del dibujo
dibujo.ylim(-0.1,0.4)

dibujo.legend()



dibujo.show()