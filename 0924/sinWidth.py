# -*- coding: utf-8 -*-
from numpy import *
import pylab as plt
 
#“linspace(開始値，終了値，分割数)”で，線形数列を作成。
x = linspace(-pi, pi, 100)
#数列をsinの引数に入れると，sin(x)の数列が生成される。
y = sin(x)
 
#plot(x, y, linewidth=1)で，線色を設定。
#plt.plot(x, y, color="y", linewidth=1)
#plt.plot(x, y, color="y", linewidth=2)
plt.plot(x, y, color="y", linewidth=3)
 
#plotした関数を表示する。
plt.show()