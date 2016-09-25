# -*- coding: utf-8 -*-
from numpy import *
import pylab as plt
 
#“linspace(開始値，終了値，分割数)”で，線形数列を作成。
x = linspace(-pi, pi, 100)
#数列をsinの引数に入れると，sin(x)の数列が生成される。
y = sin(x)
 
#plot(x, y, color="hoge")で，線色を設定。16進数コードも可能。
#plt.plot(x, y, color="#1e90ff")
#plt.plot(x, y, color="#ff8c00")
#plt.plot(x, y, color="g")
#plt.plot(x, y, color="y")
#plt.plot(x, y, color="c")
#plt.plot(x, y, color="b")
#plt.plot(x, y, color="r")
#plt.plot(x, y, color="k")
plt.plot(x, y, color="m")
#plotした関数を表示する。
plt.show()