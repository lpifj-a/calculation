import matplotlib.pyplot as plt
from sympy import *
import os


"""
str1="xsin(x)"
str2="cos(x)"
str3="sin(x)*cos(x)"
range="-5,5"
list = range.split(",")
a = float(list[0])
b = float(list[1])
print(a,b)
x = symbols('x')
try:
    y1 = sympify(str1)
    y2 = sympify(str2)
    y3 = sympify(str3)
    g = plot(y1,y2,y3,(x,a,b),ylim=(a,b),axis_center=(0,0),legend=true,aspect_ratio=(1.0,1.0),show=false)
    g[1].line_color = "red"
    g[2].line_color = "green"
    g.show()
except:
    print("a")
"""
#dy = diff(y)

str = "[-67,9]"
a = float(((str.split(","))[0]).split("[")[1])
b = float(((str.split(","))[1]).split("]")[0])
print(a+b)
