import numpy as np

class DifferentialEquations:
  def __init__(self):
    self.x = []
    self.y = []
    self.f = ""
    self.interval = []
    self.h = 0
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
    

  def set_data(self, x, y):
    self.x = x
    self.y = y

  def set_interval(self, interval):
    self.interval = interval

  def set_function(self, f):
    self.f = f

  def set_h(self, h):
    self.h = h

  def menu(self):
    while True:
      print("\nEcuaciones diferenciales ordinarias")
      print("1. Euler")
      print("2. Heun")
      print("3. Runge-Kutta de orden 2")
      print("4. Runge-Kutta de orden 3")
      print("5. Runge-Kutta de orden 4")
      print("6. Adams-Bashforth")
      print("7. Adams-Moulton")
      print("8. Salir")
      option = input("Seleccione una opción: ")

      if option == "1":
        self.euler()
      elif option == "2":
        self.heun()
      elif option == "3":
        self.runge_kutta_2()
      elif option == "4":
        self.runge_kutta_3()
      elif option == "5":
        self.runge_kutta_4()
      elif option == "6":
        order = int(input("Ingrese el orden del método de Adams-Bashforth: "))
        self.adams_bashforth(order)
      elif option == "7":
        order = int(input("Ingrese el orden del método de Adams-Moulton: "))
        self.adams_moulton(order)
      elif option == "8":
        break
      else:
        print("Opción no válida")

  def euler(self):
    x = self.interval[0]
    y = [self.y[0]]
    h = self.h
    f = self.f
    context = self.context

    while x < self.interval[1]:
      y.append(y[-1] + h * eval(f, context, {'x': x, 'y': y[-1]}))
      x += h
      self.x.append(x)
      self.y.append(y[-1])

    for i in range(len(self.x)):
      print(f"i: {i}, x: {self.x[i]}, y: {self.y[i]}")

  def heun(self):
    x = self.interval[0]
    y = [self.y[0]]
    h = self.h
    f = self.f
    context = self.context

    # Predictor
    while x < self.interval[1]:
      y_pred = y[-1] + h * eval(f, context, {'x': x, 'y': y[-1]})
      y.append(y[-1] + h/2 * (eval(f, context, {'x': x, 'y': y[-1]}) + eval(f, context ,{'x': x+h, 'y': y_pred})))
      x += h
      self.x.append(x)
      self.y.append(y[-1])

    for i in range(len(self.x)):
      print(f"i: {i}, x: {self.x[i]}, y: {self.y[i]}")

  def runge_kutta_2(self):
    x = self.interval[0]
    y = [self.y[0]]
    h = self.h
    f = self.f
    context = self.context

    while x < self.interval[1]:
      k1 = h * eval(f, context, {'x': x, 'y': y[-1]})
      k2 = h * eval(f, context, {'x': x + h, 'y': y[-1] + k1})
      y.append(y[-1] + (k1 + k2)/2)
      x += h
      self.x.append(x)
      self.y.append(y[-1])
      print(f"x_i: {x}, y_i: {y[-1]}, k1: {k1}, k2: {k2}")

    for i in range(len(self.x)):
      print(f"i: {i}, x: {self.x[i]}, y: {self.y[i]}")

  def runge_kutta_3(self):
    x = self.interval[0]
    y = [self.y[0]]
    h = self.h
    f = self.f
    context = self.context

    while x < self.interval[1]:
      k1 = h * eval(f, context, {'x': x, 'y': y[-1]})
      k2 = h * eval(f, context, {'x': x + h/2, 'y': y[-1] + k1/2})
      k3 = h * eval(f, context, {'x': x + h, 'y': y[-1] - k1*h + 2*k2*h})
      y.append(y[-1] + (k1 + 4*k2 + k3)/6)
      x += h
      self.x.append(x)
      self.y.append(y[-1])
      print(f"x_i: {x}, y_i: {y[-1]}, k1: {k1}, k2: {k2}, k3: {k3}")

    for i in range(len(self.x)):
      print(f"i: {i}, x: {self.x[i]}, y: {self.y[i]}")

  def runge_kutta_4(self):
    x = self.interval[0]
    y = [self.y[0]]
    h = self.h
    f = self.f
    context = self.context

    while x < self.interval[1]:
      k1 = h * eval(f, context, {'x': x, 'y': y[-1]})
      k2 = h * eval(f, context, {'x': x + h/2, 'y': y[-1] + k1/2})
      k3 = h * eval(f, context, {'x': x + h/2, 'y': y[-1] + k2/2})
      k4 = h * eval(f, context, {'x': x + h, 'y': y[-1] + h*k3})
      y.append(y[-1] + (k1 + 2*k2 + 2*k3 + k4)/6)
      x += h
      self.x.append(x)
      self.y.append(y[-1])
      print(f"x_i: {x}, y_i: {y[-1]}, k1: {k1}, k2: {k2}, k3: {k3}, k4: {k4}")

    for i in range(len(self.x)):
      print(f"i: {i}, x: {self.x[i]}, y: {self.y[i]}")

  def adams_bashforth(self, order):
    coeficients = {
      2: [3/2, -1/2],
      3: [23/12, -16/12, 5/12],
      4: [55/24, -59/24, 37/24, -9/24],
      5: [1901/720, -2774/720, 2616/720, -1274/720, 251/720],
      6: [4227/720, -7923/720, 9982/720, -7298/720, 2877/720, -475/720]
    }
    if order not in coeficients:
      raise ValueError("El orden debe ser 2, 3 o 4")
    
    x = self.interval[0]
    y = [self.y[0]]
    h = self.h
    f = self.f
    context = self.context
    coef = coeficients[order]

    while x < self.interval[1]:
      y_pred = y[-1] + h * eval(f, context, {'x': x, 'y': y[-1]})
      y_pred_2 = y[-1] + h * eval(f, context, {'x': x + h, 'y': y_pred})
      y_pred_3 = y[-1] + h * eval(f, context, {'x': x + 2*h, 'y': y_pred_2})
      y_pred_4 = y[-1] + h * eval(f, context, {'x': x + 3*h, 'y': y_pred_3})
      y.append(y[-1] + h * sum([coef[i] * eval(f, context, {'x': x + i*h, 'y': y_pred}) for i in range(order)]))
      x += h
      self.x.append(x)
      self.y.append(y[-1])


    for i in range(len(self.x)):
      print(f"i: {i}, x: {self.x[i]}, y: {self.y[i]}")

  def adams_moulton(self, order):
    coeficients = {
      2: [1/2, 1/2],
      3: [5/12, 8/12, -1/12],
      4: [9/24, 19/24, -5/24, 1/24],
      5: [251/720, 646/720, -264/720, 106/720, -19/720],
      6: [475/1440, 1427/1440, -798/1440, 482/1440, -173/1440, 27/1440]
    }

    if order not in coeficients:
      raise ValueError("El orden debe ser 2, 3 o 4")
    
    x = self.interval[0]
    y = [self.y[0]]
    h = self.h
    f = self.f
    context = self.context
    coef = coeficients[order]

    while x < self.interval[1]:
      y_pred = y[-1] + h * eval(f, context, {'x': x, 'y': y[-1]})
      y_pred_2 = y[-1] + h * eval(f, context, {'x': x + h, 'y': y_pred})
      y_pred_3 = y[-1] + h * eval(f, context, {'x': x + 2*h, 'y': y_pred_2})
      y_pred_4 = y[-1] + h * eval(f, context, {'x': x + 3*h, 'y': y_pred_3})
      y.append(y[-1] + h * sum([coef[i] * eval(f, context ,{'x': x + i*h, 'y': y_pred}) for i in range(order)]))
      x += h
      self.x.append(x)
      self.y.append(y[-1])

    for i in range(len(self.x)):
      print(f"i: {i}, x: {self.x[i]}, y: {self.y[i]}")
