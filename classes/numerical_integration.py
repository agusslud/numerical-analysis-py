import numpy as np

class NumericalIntegration:
  def __init__(self):
    self.interval = []
    self.f = ""
    self.n = None
    self.h = None
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

  def trapezoidal_rule(self):
    h = (self.interval[1] - self.interval[0]) / self.n
    x = np.linspace(self.interval[0], self.interval[1], self.n+1)
    y = []
    for i in range(len(x)):
      y.append(eval(self.f, self.context, {'x': x[i]}))
    y[0] /= 2
    y[-1] /= 2
    return (h / 2) * (2 * np.sum(y))
  
  def simpson_rule(self):
    pass

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
        pass
      elif option == 3:
        exit = True
      else:
        print("Opcion no valida")
