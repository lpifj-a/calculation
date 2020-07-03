import matplotlib.pyplot as plt
from sympy import *
import os



str="xlog(x)"

x = symbols('x')
try:
    y = sympify(str)
    g = plotting.plot(y)
except:
    print("a")
#dy = diff(y)
if 1:
    print("aaa\n\n"\
         "aaaaaaa")
