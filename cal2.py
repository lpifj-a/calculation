import matplotlib.pyplot as plt
from sympy import *
import os
from PIL import Image

str="x^2"

x = symbols('x')
y = sympify(str)
dy = diff(y)
g = plotting.plot(y)
g.save("a.png")
img = Image.open('a.png')
rgb_img = img.convert('RGB')
rgb_img.save('a.jpg')
