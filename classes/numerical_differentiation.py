import numpy as np

class NumericalDifferentiation:
  def __init__(self):
    self.x = []
    self.y = []
    self.interval = []
    self.f = ""
    self.h = None
    self.y_prime = []

  def set_data(self, x, y):
    self.x = x
    self.y = y

  def set_interval(self, interval):
    self.interval = interval

  def set_function(self, f):
    self.f = f

  def set_h(self, h):
    self.h = h

  def three_points_forward(self, x_0):
    return (-3*self.y[x_0] + 4*self.y[x_0+1] - self.y[x_0+2]) / (2*self.h)

  def three_points_backward(self, x_0):
    return (3*self.y[x_0] - 4*self.y[x_0-1] + self.y[x_0-2]) / (2*self.h)

  def three_points_centered(self, x_0):
    return (self.y[x_0+1] - self.y[x_0-1]) / (2*self.h)

  def five_points_forward(self, x_0):
    return (-25*self.y[x_0] + 48*self.y[x_0+1] - 36*self.y[x_0+2] + 16*self.y[x_0+3] - 3*self.y[x_0+4]) / (12*self.h)

  def five_points_backward(self, x_0):
    return (25*self.y[x_0] - 48*self.y[x_0-1] + 36*self.y[x_0-2] - 16*self.y[x_0-3] + 3*self.y[x_0-4]) / (12*self.h)

  def five_points_centered(self, x_0):
    return (self.y[x_0-2] - 8*self.y[x_0-1] + 8*self.y[x_0+1] - self.y[x_0+2]) / (12*self.h)
  
  def print_points(self):
    for i in range(len(self.x)):
      print(f"f'({self.x[i]}) = {self.y_prime[i]}")

  def menu(self):
    x = []
    y = []
    f = ""
    exit = False

    context = {
      'np': np,
      'e': np.e,
      'pi': np.pi,
      'sin': np.sin,
      'cos': np.cos,
      'tan': np.tan,
      'log': np.log,
      'exp': np.exp,
      'sqrt': np.sqrt,
      'abs': np.abs,
    }

    print("Ingrese la funcion f(x) a diferenciar")
    f = input("f(x) = ")
    self.set_function(f)

    if f == "":
      print("Ingrese los puntos (x, y) de la funcion")
      n = int(input("Numero de puntos: "))

      for i in range(n):
        x.append(float(input(f"x[{i}] = ")))
        y.append(float(input(f"y[{i}] = ")))
      self.set_data(x, y)

      h = float(input("Ingrese el valor de crecimiento h: "))
      if self.x[1] - self.x[0] == h:
        self.set_h(h)
      else:
        print("El valor de h no es valido")
        return
    else:
      print("Ingrese el intervalo de diferenciacion")
      a = float(input("a = "))
      b = float(input("b (ingrese un valor mas) = "))
      self.set_interval([a, b])

      print("Ingrese el valor de crecimiento h")
      h = float(input("h = "))
      self.set_h(h)

      for i in np.arange(a, b, h):
        x.append(i)
        y.append(eval(f, context, {'x': i}))
        print(f"x = {i}, f(x) = {y[-1]}")
      self.set_data(x, y)

    while not exit:
      print("Menu de diferenciacion numerica")
      print("1. Tres puntos")
      print("2. Cinco puntos")
      print("3. Salir")

      option = int(input("Seleccione una opcion: "))
      if option == 1:
        for i in range(len(self.x)):
          if i == 0:
            self.y_prime.append(self.three_points_forward(i))
            print(f"f'({self.x[i]}) = {self.y_prime[i]}")
          elif i == len(self.x) - 1:
            self.y_prime.append(self.three_points_backward(i))
            print(f"f'({self.x[i]}) = {self.y_prime[i]}")
          else:
            self.y_prime.append(self.three_points_centered(i))
            print(f"f'({self.x[i]}) = {self.y_prime[i]}")
      elif option == 2:
        for i in range(len(self.x)):
          if i == 0:
            self.y_prime.append(self.five_points_forward(i))
            print(f"f'({self.x[i]}) = {self.y_prime[i]}")
          elif i == 1:
            self.y_prime.append(self.five_points_forward(i))
            print(f"f'({self.x[i]}) = {self.y_prime[i]}")
          elif i == len(self.x) - 1:
            self.y_prime.append(self.five_points_backward(i))
            print(f"f'({self.x[i]}) = {self.y_prime[i]}")
          elif i == len(self.x) - 2:
            self.y_prime.append(self.five_points_backward(i))
            print(f"f'({self.x[i]}) = {self.y_prime[i]}")
          else:
            self.y_prime.append(self.five_points_centered(i))
            print(f"f'({self.x[i]}) = {self.y_prime[i]}")
      elif option == 3:
        exit = True
      else:
        print("Opcion no valida")
