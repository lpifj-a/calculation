import matplotlib.pyplot as plt
from sympy import *
import os

str="x^2"

x = symbols('x')
y = sympify(str)
dy = diff(y)
g = plotting.plot(y)
print(os.getcwd())
g.save("a.png")
