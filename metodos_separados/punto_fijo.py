from math import *

def g(x):
  return e**(-x)

def punto_fijo(x0, tol, n):
  for i in range(n):
      x1 = g(x0)
      if abs(x1 - x0) < tol:
        print("x", i+1, " = ", x1, " es un punto fijo")
        return
      x0 = x1
      print("x", i+1, " = ", x1)

punto_fijo(0, 10**(-3), 100)