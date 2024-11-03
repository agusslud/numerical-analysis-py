from math import *

def f(x):
  func = e**(-x)-x
  return func

def df(x):
  func = -e**(-x)-1
  return func

def newton_raphson(x0, tol, n):
  for i in range(n):
    x1 = x0 - f(x0)/df(x0)
    if abs(x1-x0) < tol:
      print("x", i+1, "=", x1, "es la raíz")
      return
    x0 = x1
    print("x", i+1, "=", x1)

newton_raphson(0, 10**(-3), 100)