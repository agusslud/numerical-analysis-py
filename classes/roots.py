import sympy as sp

class Roots:
  def __init__(self):
    self.expression = ""
    self.roots = []
    self.intervals = []

  def set_expression(self):
    expression = input("Enter the expression: ")
    self.expression = sp.sympify(expression)

  def get_expression(self):
    return self.expression
  
  def get_roots(self):
    return self.roots
  
  def get_intervals(self):
    return self.intervals

  def calculate_intervals(self, max_roots, start, end):
    fa = self.expression.subs(self.expression, start)
    fb = self.expression.subs(self.expression, end)

    for i in range(max_roots):
      if fa * fb < 0:
        self.intervals.append((start, end))
      start = end
      end += 1
      fa = self.expression.subs(self.expression, start)
      fb = self.expression.subs(self.expression, end)
  
  def bisection(self):
    # Get the expression
    self.set_expression()
    # Get the intervals
    print("Ingrese desde donde quiere empezar a buscar las raices: ")
    start = int(input())
    print("Ingrese hasta donde quiere buscar las raices: ")
    end = int(input())
    print("Ingrese el numero de raices que quiere encontrar: ")
    max_roots = int(input())
    self.calculate_intervals(max_roots, start, end)

    for interval in self.intervals:
      a, b = interval
      fa = self.expression.subs(self.expression, a)
      fb = self.expression.subs(self.expression, b)
      c = (a + b) / 2
      fc = self.expression.subs(self.expression, c)
      while abs(fc) > 0.0001:
        if fa * fc < 0:
          b = c
          fb = fc
        else:
          a = c
          fa = fc
        c = (a + b) / 2
        fc = self.expression.subs(self.expression, c)
      self.roots.append(c)

    print("Las raices son: ", self.roots)

  def fixed_point(self):
    pass

  def newton_raphson(self):
    pass

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
