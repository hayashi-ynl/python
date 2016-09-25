# -*- coding: utf-8 -*-
from numpy import *
import pylab as plt
 
#“linspace(開始値，終了値，分割数)”で，線形数列を作成。
x = linspace(-pi, pi, 50)
#数列をsinの引数に入れると，sin(x)の数列が生成される。
y = sin(x)
 
#グラフ描画
plt.plot(x, y, color="b", linewidth=3)
 
#軸タイトルを設定
# "$\<書体>{}$" で設定すると，下付きや上付きを指定できる。
# 立体： $\mathsf{ hoge }$
# 斜体： $\it{ hoge }$
#などなど。
plt.xlabel("Drain Voltage $\it{V_{DS}}$ (V)",fontsize=22)
plt.ylabel("Drain Current $\it{I_{DS}}$ (mA)",fontsize=22)
 
#plotした関数を表示する。
plt.show()