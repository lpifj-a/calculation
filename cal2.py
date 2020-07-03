import matplotlib.pyplot as plt
from sympy import *
import os


str="xlog("

x = symbols('x')
y = sympify(str)
#dy = diff(y)
"""
try :
    g = plotting.plot(y)
except TypeError as e:
    text = "Error"
"""
print(diff(y))
