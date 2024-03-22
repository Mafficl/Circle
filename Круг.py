from math import *
print("Круг")
r = float(input("Радиус = "))
d = r*2
S = pi*r**2
S = round (S, 5)
c = 2*pi*r
c = round (c, 5)
print ("Диаметр = ", d)
print('Площадь = ', S)
print('Длина окружности = ', c)