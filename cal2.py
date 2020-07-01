import matplotlib.pyplot as plt
from sympy import *


str="x^2"

x = symbols('x')
y = sympify(str)
dy = diff(y)
g = plotting.plot(y)
g.save("a.png")
