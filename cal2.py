import matplotlib.pyplot as plt
from sympy import *

str=input(">")

x = symbols('x')
y = sympify(str)
#plotting.plot(y)
pprint(y)
pprint(diff(y))
