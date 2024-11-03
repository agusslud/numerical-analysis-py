import numpy as np
import sympy as sp

class Roots:
  def __init__(self):
    self.expression = ""
    self.intervals = [[]]
    self.tolerance = 10**(-3)
    self.context = {
      'np': np,
      'e': np.e,
      'pi': np.pi,
      'sin': np.sin,
      'cos': np.cos,
      'tan': np.tan,
      'log': np.log,
      'exp': np.exp
    }

  def set_expression(self, expression):
    self.expression = expression

  def set_intervals(self, intervals):
    self.intervals = intervals

  def set_tolerance(self, error):
    self.error = error

  def get_expression(self):
    return self.expression
  
  def get_intervals(self):
    return self.intervals
  
  def get_tolerance(self):
    return self.tolerance

  def bisection(self):
    if len(self.intervals) == 0:
      print("Primero calcule los intervalos")
      return

    for interval in self.intervals:
      a, b = interval
      fa = self.expression.subs('x', a)
      fb = self.expression.subs('x', b)

      if fa * fb > 0:
        print("No hay raices en el intervalo")
        continue

      print(f"Intervalo inicial: [{a}, {b}]")
      print(f"f(a): {fa}, f(b): {fb}")

      while True:
        c = (a + b) / 2
        fc = self.expression.subs('x', c)

        print(f"Nuevo punto medio: c = {c}")
        print(f"f(c): {fc}")

        if abs(fc) < self.error:
          break

        if fa * fc < 0:
          b = c
          fb = fc
          print(f"Nuevo intervalo: [{a}, {b}]")
        else:
          a = c
          fa = fc
          print(f"Nuevo intervalo: [{a}, {b}]")

      print("\nLa raiz es: ", c, "\n")

  def fixed_point(self):
    max_iterations = 100

    if len(self.intervals) == 0:
      print("Primero calcule los intervalos")
      return
    
    for interval in self.intervals:
      a, b = interval
      fa = eval(self.expression, self.context, {'x': a})
      fb = eval(self.expression, self.context, {'x': b})

      if fa * fb > 0:
        print("No hay raices en el intervalo")
        continue

      print(f"Intervalo inicial: [{a}, {b}]")
      print(f"f(a): {fa}, f(b): {fb}")

      # asumimos que expression es una funcion g(x)

      for i in range(max_iterations):
        c = eval(self.expression, self.context, {'x': a})
        fc = eval(self.expression, self.context, {'x': c})

        print(f"Nuevo punto: c = {c}")
        print(f"f(c): {fc}")

        if abs(fc) < self.tolerance:
          break

        a = c

      print("\nLa raiz es: ", c, "\n")

  def newton_raphson(self):
    if len(self.intervals) == 0:
      print("Primero calcule los intervalos")
      return

    for interval in self.intervals:
      a, b = interval
      fa = self.expression.subs('x', a)
      fb = self.expression.subs('x', b)

      if fa * fb > 0:
        print("No hay raices en el intervalo")
        continue

      print(f"Intervalo inicial: [{a}, {b}]")
      print(f"f(a): {fa}, f(b): {fb}")

      x = sp.symbols('x')
      f_prime = sp.diff(self.expression, x)
      g = x - self.expression / f_prime

      while True:
        c = g.subs('x', a)
        fc = self.expression.subs('x', c)

        print(f"Nuevo punto: c = {c}")
        print(f"f(c): {fc}")

        if abs(fc) < self.error:
          break

        a = c

      print("\nLa raiz es: ", c, "\n")

  def secant(self):
    pass

  def handle_invalid_option(self):
    print("Opcion no valida")
  
  def menu(self):
    options = {
      1: self.bisection,
      2: self.fixed_point,
      3: self.newton_raphson,
      4: self.secant
    }

    while True:
      print("Menu de raices de ecuaciones")
      print("1. Metodo de biseccion")
      print("2. Metodo de punto fijo")
      print("3. Metodo de Newton-Raphson")
      print("4. Metodo de la secante")
      print("5. Regresar al menu principal")

      option = int(input("Seleccione una opcion: "))

      if option == 5:
        break

      selected_option = options.get(option, self.handle_invalid_option)
      selected_option()
