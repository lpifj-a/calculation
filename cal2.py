import matplotlib.pyplot as plt
from sympy import *


str="x"

x = symbols('x')
y = sympify(str)
dy = diff(y)
str=print(y)
print(type(str))
