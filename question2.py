"""Cette fonction permet de calculer la valeur de e"""

import math

def calculExponentiel():
    e = 0
    for i in range(0,100):
      e = e + 1/math.factorial(i)
    print(e)

calculExponentiel()      
