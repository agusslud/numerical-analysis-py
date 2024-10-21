from classes.curve_fitting import CurveFitting
from classes.numerical_differentiation import NumericalDifferentiation
from classes.numerical_integration import NumericalIntegration
from classes.roots import Roots
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
  interval = [1.1699, 5]
  f = "1-x-4*x**(3)+3*x**(5)"
  n = 10

  numerical_integration.set_interval(interval)
  numerical_integration.set_function(f)
  numerical_integration.set_n(n)
  # menu
  numerical_integration.menu()

def handle_differential_equations():
  print("Ecuaciones diferenciales ordinarias")

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

main_menu()