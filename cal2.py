import matplotlib.pyplot as plt
from sympy import *
import os


str="x*log(x)"

x = symbols('x')
y = sympify(str)
dy = diff(y)
a=sstr(y)
print(type(a))
