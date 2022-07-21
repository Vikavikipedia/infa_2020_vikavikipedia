'''
import math
import cmath
print(math.sin(math.pi))
print(cmath.sin(math.pi))
x = 1 + 1j
print(cmath.sin(x))
print(math.sin(x))

from cmath import *
from math import *
help(sin)
print(sin(1))

from math import *
from cmath import *
help(sin)
print(sin(1))

import cmath as cm
import math as m
print(m.sin(m.pi))
print(cm.sin(m.pi))

import house
house.main()
house.draw_house()
'''


class Goat:
    age = 0

    def pet():
        print('Hello')


class Cow:
    pass


a = Goat()
b = Goat()
a.pet()
b.pet()
a.age = 5
b.age = 3
