import numpy as np

class NumericalIntegration:
  def __init__(self):
    self.interval = []
    self.f = ""
    self.n = None
    self.h = None
    self.x = []
    self.y = []
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

  def set_interval(self, interval):
    self.interval = interval

  def set_function(self, f):
    self.f = f

  def set_n(self, n):
    self.n = n

  def set_h(self, h):
    self.h = h

  def set_data(self, x, y):
    self.x = x
    self.y = y

  def trapezoidal_rule(self):
    if len(self.x) > 0 and len(self.y) > 0:
      h = (self.x[-1] - self.x[0]) / (len(self.x) - 1)
      y = self.y.copy()
    else:
      h = (self.interval[1] - self.interval[0]) / self.n
      self.x = np.linspace(self.interval[0], self.interval[1], self.n+1)
      self.y = [eval(self.f, self.context, {'x': xi}) for xi in self.x]
      y = self.y.copy()

    y[0] /= 2
    y[-1] /= 2

    return (h / 2) * (2 * np.sum(y))
  
  def simpson_rule(self):
    if len(self.x) > 0 and len(self.y) > 0:
      h = (self.x[-1] - self.x[0]) / (len(self.x) - 1)
      y = self.y.copy()
    else:
      h = (self.interval[1] - self.interval[0]) / self.n
      self.x = np.linspace(self.interval[0], self.interval[1], self.n+1)
      self.y = [eval(self.f, self.context, {'x': xi}) for xi in self.x]
      y = self.y.copy()

    y[0] /= 3
    y[-1] /= 3

    print(f"h: {h}")
    print(f"y[0]: {y[0]}, y[-1]: {y[-1]}")

    odd = 0
    even = 0
    for i in range(1, len(y) - 1):
      if i % 2 == 0:
        even += y[i]
        print(f"par (y[{i}]): {y[i]}, suma_par: {even}")
      else:
        odd += y[i]
        print(f"impar (y[{i}]): {y[i]}, suma_impar: {odd}")

    return (h / 3) * (y[0] + 4 * odd + 2 * even + y[-1])

  def print_integral(self, integral):
    print(f"Integral: {integral}")

  def menu(self):
    exit = False

    while not exit:
      print("Metodos de integracion numerica")
      print("1. Regla del trapecio")
      print("2. Regla de Simpson")
      print("3. Salir")
      option = int(input("Opcion: "))

      if option == 1:
        integral = self.trapezoidal_rule()
        self.print_integral(integral)
      elif option == 2:
        integral = self.simpson_rule()
        self.print_integral(integral)
      elif option == 3:
        exit = True
      else:
        print("Opcion no valida")
