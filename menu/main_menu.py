from classes.roots import Roots
from classes.curve_fitting import CurveFitting
from classes.numerical_differentiation import NumericalDifferentiation
from classes.numerical_integration import NumericalIntegration
from classes.differential_equations import DifferentialEquations
import numpy as np

def handle_roots():
  roots = Roots()
  # menu
  roots.menu()

def handle_equation_system():
  print("Sistema de ecuaciones")

def handle_curve_fitting():
  curve_fitting = CurveFitting()
  # upload data
  x = [0, 1, 2, 3]
  y = [1, 2.7182, 7.3891, 20.0855]
  curve_fitting.set_data(x, y)
  # menu
  curve_fitting.menu()

def handle_numerical_differentiation():
  numerical_differentiation = NumericalDifferentiation()
  numerical_differentiation.menu()

def handle_numerical_integration():
  numerical_integration = NumericalIntegration()
  # upload data
  x = []
  y = []
  f = "8+5*cos(x)"

  if f == "":
    x = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
    y = [1, 7, 4, 3, 5, 9]

    n = len(x)

    if n == len(y):
      numerical_integration.set_n(n)
    else:
      print("Los arreglos x y y deben tener la misma longitud")

    numerical_integration.set_data(x, y)
    
  else:
    interval = [0, np.pi]
    n = 10
    
    numerical_integration.set_interval(interval)
    numerical_integration.set_function(f)
    numerical_integration.set_n(n)

  # menu
  numerical_integration.menu()

def handle_differential_equations():
  differential_equations = DifferentialEquations()
  # upload data
  # initial conditions
  x = [0]
  y = [2]
  f = "e**(0.8*x) - 0.5*y"
  interval = [0, 4]
  h = 0.1

  differential_equations.set_data(x, y)
  differential_equations.set_function(f)
  differential_equations.set_interval(interval)
  differential_equations.set_h(h)
  # menu
  differential_equations.menu()

def handle_exit():
  global exit_program
  exit_program = True

def handle_invalid_option():
  print("Opcion no valida")

def main_menu():
  global exit_program
  exit_program = False

  options = {
    1: handle_roots,
    2: handle_equation_system,
    3: handle_curve_fitting,
    4: handle_numerical_differentiation,
    5: handle_numerical_integration,
    6: handle_differential_equations,
    7: handle_exit
  }

  while not exit_program:
    print("Menu principal")
    print("1. Raices de ecuaciones")
    print("2. Sistema de ecuaciones")
    print("3. Ajuste de curvas")
    print("4. Diferenciacion numerica")
    print("5. Integracion numerica")
    print("6. Ecuaciones diferenciales ordinarias")
    print("7. Salir")

    option = int(input("Seleccione una opcion: "))

    selected_option = options.get(option, handle_invalid_option)
    selected_option()
