# -*- coding: utf-8 -*-
# date : 2016-09-25
# name : Masaki.H
# -----------------------------------------------------------------------------
# Inspired by "ticklabels_demo_rotation.py"
# http://matplotlib.org/examples/ticks_and_spines/ticklabels_demo_rotation.html
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
        
#    for p in DateArray:
#        print p
#        
#    for q in TempArray:
#        print q

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y = TempArray
labels = DateArray

plt.plot(x, y, 'ro')
plt.title("Mito-city avg Temperature")
# You can specify a rotation for the tick labels in degrees or with keywords.
plt.xticks(x, labels, rotation='vertical')
#plt.xticks(x, labels, rotation=45)
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)
plt.show()