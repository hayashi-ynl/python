# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import deque

DateArray = []
TempArray = []

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    
    time = 0
    for row in reader:
        if time > 4 :
            date, temp, a, b = row
            DateArray.append(date)
            TempArray.append(temp)
            #print DateArray, TempArray
        time = time + 1
        
    for p in DateArray:
        print p
        
#    for q in TempArray:
#        print q

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = TempArray
labels = DateArray

#plt.plot(x, y, 'ro')
#plt.show()