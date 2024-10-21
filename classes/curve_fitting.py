import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

class CurveFitting:
  def __init__(self):
    self.x = []
    self.y = []
    self.coefficients = []
    self.expression = ""
    self.fp0 = None
    self.fpn = None

  def set_boundary_conditions(self, fp0, fpn):
    self.fp0 = fp0
    self.fpn = fpn

  def set_data(self, x, y):
    self.x = x
    self.y = y

  def set_expression(self, expression):
    self.expression = expression

  def plot_data(self):
    plt.plot(self.x, self.y, 'o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

  def linear_regression(self):
    n = len(self.x)
    
    print("Que tipo de regresion desea realizar?")
    print("1. Lineal")
    print("2. Exponencial")
    print("3. Potencial")
    print("4. Crecimiento")

    option = int(input("Opcion: "))

    if option == 1:
      sum_x = sum(self.x)
      sum_y = sum(self.y)
      sum_x2 = sum([x**2 for x in self.x])
      sum_xy = sum([x*y for x, y in zip(self.x, self.y)])
      print(f"sum_x: {sum_x}, sum_y: {sum_y}, sum_x2: {sum_x2}, sum_xy: {sum_xy}")
      self.linear_regression_lineal(n, sum_x, sum_y, sum_x2, sum_xy)

      print(f"y = {self.coefficients[0]}x + {self.coefficients[1]}")

      x = np.linspace(min(self.x), max(self.x), 100)
      y = self.coefficients[0]*x + self.coefficients[1]

      plt.plot(self.x, self.y, 'o', label='Datos')
      plt.plot(x, y, label='Regresion lineal')
      plt.xlabel('x')
      plt.ylabel('y')
      plt.legend()
      plt.show()
    elif option == 2:
      sum_x = sum(self.x)
      # use the natural logarithm of y
      sum_y = sum([np.log(y) for y in self.y])
      sum_x2 = sum([x**2 for x in self.x])
      # use the natural logarithm of y
      sum_xy = sum([x*np.log(y) for x, y in zip(self.x, self.y)])
      print(f"sum_x: {sum_x}, sum_y: {sum_y}, sum_x2: {sum_x2}, sum_xy: {sum_xy}")
      self.linear_regression_lineal(n, sum_x, sum_y, sum_x2, sum_xy)

      B = self.coefficients[0]
      A = np.exp(self.coefficients[1])

      print(f"y = {A}e^{B}x")

      x = np.linspace(min(self.x), max(self.x), 100)
      y = A*np.exp(B*x)

      plt.plot(self.x, self.y, 'o', label='Datos')
      plt.plot(x, y, label='Regresion exponencial')
      plt.xlabel('x')
      plt.ylabel('y')
      plt.legend()
      plt.show()
    elif option == 3:
      # use the natural logarithm of x and y
      sum_x = sum([np.log10(x) for x in self.x])
      sum_y = sum([np.log10(y) for y in self.y])
      sum_x2 = sum([np.log10(x)**2 for x in self.x])
      sum_xy = sum([np.log10(x)*np.log10(y) for x, y in zip(self.x, self.y)])
      print(f"sum_x: {sum_x}, sum_y: {sum_y}, sum_x2: {sum_x2}, sum_xy: {sum_xy}")
      self.linear_regression_lineal(n, sum_x, sum_y, sum_x2, sum_xy)

      B = self.coefficients[0]
      A = 10**self.coefficients[1]

      print(f"y = {A}x^{B}")

      x = np.linspace(min(self.x), max(self.x), 100)
      y = A*x**B

      plt.plot(self.x, self.y, 'o', label='Datos')
      plt.plot(x, y, label='Regresion potencial')
      plt.xlabel('x')
      plt.ylabel('y')
      plt.legend()
      plt.show()
    elif option == 4:
      # use 1/x and 1/y
      sum_x = sum([1/x for x in self.x])
      sum_y = sum([1/y for y in self.y])
      sum_x2 = sum([1/x**2 for x in self.x])
      sum_xy = sum([1/x*1/y for x, y in zip(self.x, self.y)])
      print(f"sum_x: {sum_x}, sum_y: {sum_y}, sum_x2: {sum_x2}, sum_xy: {sum_xy}")
      self.linear_regression_lineal(n, sum_x, sum_y, sum_x2, sum_xy)

      print(f"y = {self.coefficients[0]} * x/({self.coefficients[1]} + x)")

      x = np.linspace(min(self.x), max(self.x), 100)
      y = self.coefficients[0]*x/(self.coefficients[1] + x)

      plt.plot(self.x, self.y, 'o', label='Datos')
      plt.plot(x, y, label='Regresion de crecimiento')
      plt.xlabel('x')
      plt.ylabel('y')
      plt.legend()
      plt.show()

  def linear_regression_lineal(self, n, sum_x, sum_y, sum_x2, sum_xy):
    a_1 = ((n*sum_xy) - (sum_x*sum_y)) / ((n*sum_x2) - (sum_x**2))
    a_0 = (sum_y - a_1*sum_x) / n

    print(f"a_1: {a_1}, a_0: {a_0}")
      
    self.coefficients = [a_1, a_0]

  def divided_differences(self):
    n = len(self.x)

    table = np.zeros((n, n+1))

    for i in range(n):
      table[i][0] = self.y[i]

    for j in range(1, n):
      for i in range(n-j):
        table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (self.x[i+j] - self.x[i])
        print(f"table[{i}][{j}]: {table[i][j]}")
    
    return [table[0][i] for i in range(n)]

  def newton_interpolation(self):
    coefficients = self.divided_differences()
    n = len(coefficients)
    polynom_str = f"{coefficients[0]}"
    print(f"Coeficiente inicial: {coefficients[0]}")

    for i in range(1, n):
      term = f"{coefficients[i]}"
      for j in range(i):
        term += f"*(x - {self.x[j]})"
      polynom_str += " + " + term
      print(f"Termino {i}: {term}")

    x = sp.symbols('x')
    polynom = sp.sympify(polynom_str)

    print(f"Polinomio de interpolacion de Newton: {polynom}")

    # Plot

    x_vals = np.linspace(min(self.x), max(self.x), 100)
    y_vals = [eval(polynom_str) for x in x_vals]

    plt.plot(self.x, self.y, 'o', label='Datos')
    plt.plot(x_vals, y_vals, label=f"Interpolacion de Newton")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

  def lagrange_polynomial(self):
    n = len(self.x)
    x = sp.symbols('x')
    polynom = 0

    for i in range(n):
      term = self.y[i]
      print(f"Termino inicial para i={i}: {term}")

      for j in range(n):
        if i != j:
          term *= (x - self.x[j]) / (self.x[i] - self.x[j])
      polynom += term

    print(f"Polinomio de Lagrange: {polynom}")

    # Plot

    x_vals = np.linspace(min(self.x), max(self.x), 100)
    y_vals = [polynom.subs('x', x_val) for x_val in x_vals]

    plt.plot(self.x, self.y, 'o', label='Datos')
    plt.plot(x_vals, y_vals, label=f"Polinomio de Lagrange")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

  def cubic_splines(self):
    print("Que tipo de spline desea realizar?")
    print("1. Natural")
    print("2. Condicionado")

    option = int(input("Opcion: "))

    if option == 1:
      self.natural_cubic_splines()
    elif option == 2:
      self.conditioned_cubic_splines()

  def natural_cubic_splines(self):
    n = len(self.x)
    x = sp.symbols('x')

    # Step 1
    h = [self.x[i+1] - self.x[i] for i in range(n-1)]

    # Step 2
    alpha = [0] * (n-1)
    for i in range(1, n-1):
      alpha[i] = 3/h[i] * (self.y[i+1] - self.y[i]) - 3/h[i-1] * (self.y[i] - self.y[i-1])

    # Step 3
    l = [1] + [0] * (n-1)
    mu = [0] * (n-1)
    z = [0] * n
    c = [0] * n

    for i in range(1, n-1):
      l[i] = 2*(self.x[i+1] - self.x[i-1]) - h[i-1]*mu[i-1]
      mu[i] = h[i]/l[i]
      z[i] = (alpha[i] - h[i-1]*z[i-1])/l[i]

    l[-1] = 1
    z[-1] = 0
    c[-1] = 0

    # Step 4
    b = [0] * (n-1)
    d = [0] * (n-1)
    a = self.y[:n-1]

    for j in range(n-2, -1, -1):
      c[j] = z[j] - mu[j]*c[j+1]
      b[j] = (self.y[j+1] - self.y[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3
      d[j] = (c[j+1] - c[j])/(3*h[j])

    # Step 5
    splines = []
    for j in range(n-1):
      spline = f"{a[j]} + {b[j]}*(x - {self.x[j]}) + {c[j]}*(x - {self.x[j]})**2 + {d[j]}*(x - {self.x[j]})**3"
      splines.append(spline)

    print("Splines cubicos naturales:")
    for i in range(n-1):
      print(f"Spline {i}: {splines[i]}")

    # Plot

    x_vals = []
    y_vals = []

    for i in range(0, n-1):
      x_vals += np.linspace(self.x[i], self.x[i+1], 100).tolist()
      y_vals += [eval(splines[i]) for x in np.linspace(self.x[i], self.x[i+1], 100)]

    plt.plot(self.x, self.y, 'o', label='Datos')
    plt.plot(x_vals, y_vals, label=f"Splines cubicos naturales")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

  def conditioned_cubic_splines(self):
    print("Ingrese las condiciones de frontera:")
    fp0 = float(input("f'(x0) = "))
    fpn = float(input("f'(xn) = "))

    self.set_boundary_conditions(fp0, fpn)

    n = len(self.x)
    x = sp.symbols('x')

    # Step 1
    h = [self.x[i+1] - self.x[i] for i in range(n-1)]

    # Step 2
    alpha = [0] * n
    alpha[0] = 3/h[0] * (self.y[1] - self.y[0]) - 3*self.fp0
    alpha[-1] = 3*self.fpn - 3*(self.y[-1] - self.y[-2]) / h[-2]

    for i in range(1, n-1):
      alpha[i] = (3/h[i]) * (self.y[i+1] - self.y[i]) - (3/h[i-1]) * (self.y[i] - self.y[i-1])

    # Step 3
    l = [1] + [0] * (n-1)
    mu = [0] * (n-1)
    z = [0] * n
    c = [0] * n

    l[0] = 2 * h[0]
    mu[0] = 0.5
    z[0] = alpha[0] / l[0]

    for i in range(1, n-1):
      l[i] = 2 * (self.x[i+1] - self.x[i-1]) - h[i-1] * mu[i-1]
      mu[i] = h[i] / l[i]
      z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]

    l[-1] = h[-1] * (2 - mu[-2])
    z[-1] = (alpha[-1] - h[-2] * z[-2]) / l[-1]

    # Step 4
    b = [0] * (n-1)
    d = [0] * (n-1)
    a = self.y[:n-1]

    for j in range(n-2, -1, -1):
      c[j] = z[j] - mu[j] * c[j+1]
      b[j] = (self.y[j+1] - self.y[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
      d[j] = (c[j+1] - c[j]) / (3 * h[j])

    # Step 5
    splines = []

    for j in range(n-1):
      spline = f"{a[j]} + {b[j]}*(x - {self.x[j]}) + {c[j]}*(x - {self.x[j]})**2 + {d[j]}*(x - {self.x[j]})**3"
      splines.append(spline)

    print("Splines cubicos condicionados:")
    for i in range(n-1):
      print(f"Spline {i}: {splines[i]}")

    # Plot

    x_vals = []
    y_vals = []

    for i in range(0, n-1):
      x_vals += np.linspace(self.x[i], self.x[i+1], 100).tolist()
      y_vals += [eval(splines[i]) for x in np.linspace(self.x[i], self.x[i+1], 100)]

    plt.plot(self.x, self.y, 'o', label='Datos')
    plt.plot(x_vals, y_vals, label=f"Splines cubicos condicionados")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

  def menu(self):
    exit_menu = False

    options = {
      1: self.linear_regression,
      2: self.newton_interpolation,
      3: self.lagrange_polynomial,
      4: self.cubic_splines,
      5: self.plot_data,
      6: lambda: print("Salir")
    }

    while not exit_menu:
      print("Menu de ajuste de curvas")
      print("1. Regresion lineal")
      print("2. Interpolacion de Newton")
      print("3. Polinomio de Lagrange")
      print("4. Splines cubicos")
      print("5. Graficar los puntos")
      print("6. Salir")

      option = int(input("Opcion: "))

      if option in options:
        options[option]()
        if option == 6:
          exit_menu = True
      else:
        print("Opcion no valida")
