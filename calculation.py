import re
import matplotlib.pyplot as plt
import math
import numpy as np

#多項式の各項をリストに要素として格納する
def spl(str):
    mono = []
    j = 0
    for i in range(len(str)):
        if str[i] == "+":
            mono.append(str[j:i])
            j = i+1
        elif str[i] == "-":
            if i == 0:
                continue
            else:
                mono.append(str[j:i])
                j = i
        elif i == len(str)-1:
            mono.append(str[j:i+1])
    return mono

#文字列で与えられた各項の型を変換する
def change(str):
    nlist = spl(str)
    ilist = [0,0,0,0,0,0]
    j = 0
    for i in range(len(nlist)):
        coe = 0
        l = len(nlist[i])
        # 一次の項の処理
        if nlist[i][-1] == "x":
            if nlist[i][0] == "-":
                for j in range(l-2):
                    coe += -int(nlist[i][j+1])*10**((l-3)-j)
                ilist[1] = coe
            else :
                for j in range(l-1):
                    coe += int(nlist[i][j])*10**((l-2)-j)
                if coe == 0: #係数が1のとき
                    coe = 1
                ilist[1] = coe
        else :
            #二次以上の項の処理
            if "x" in nlist[i]:
                if "-" in nlist[i]:
                    for j in range(l-4):
                        coe += -int(nlist[i][j+1])*10**((l-5)-j)
                    k = int(nlist[i][-1])
                    if coe == 0:
                        coe = -1
                    ilist[k] = coe
                else:
                    for j in range(l-3):
                        coe += int(nlist[i][j])*10**((l-4)-j)
                    k = int(nlist[i][-1])
                    if coe == 0:
                        coe = 1
                    ilist[k] = coe
            #定数項の処理
            else :
                if "-" in nlist[i]:
                    for j in range(l-1):
                        coe += int(nlist[i][j+1])*10**((l-2)-j)
                    ilist[0] = int (nlist[i])
                else:
                    for j in range(l):
                        coe -= int(nlist[i][j])*10**((l-1)-j)
                    ilist[0] = int (nlist[i])

    return ilist


def plot(str):
    x = np.linspace(-5,5,100)
    nlist = change(str)
    y = nlist[5]*x**5 + nlist[4]*x**4+ nlist[3]*x**3 + nlist[2]*x**2 + nlist[1]*x + nlist[0]
    plt.plot(x,y)
    plt.show()

def change2(str):
    nlist = spl(str)
    x = np.linspace(-5,5,100)
    nlist[0] = x
    nlist[1] = -x**3
    y = 0
    for i in range(len(nlist)):
        y += nlist[i]
    return y


def plot2(str):
    x = np.linspace(-5,5,100)
    y = change3(str)
    plt.plot(x,y)
    plt.show()

#str = input(">")
str = "4*x+4"
plot2(str)
