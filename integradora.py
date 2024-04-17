import math
import matplotlib.pyplot as plt

# Método de Euler
def euler_method(f, x0, y0, h, n):
    points = [(x0, y0)]
    x = x0
    y = y0
    for _ in range(n):
        y += h * f(x, y)
        x += h
        points.append((x, y))
    return points

# Método de Euler mejorado
def improved_euler_method(f, x0, y0, h, n):
    points = [(x0, y0)]
    x = x0
    y = y0
    for _ in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y += (k1 + k2) / 2
        x += h
        points.append((x, y))
    return points

# Método de Runge-Kutta de cuarto orden
def runge_kutta(f, x0, y0, h, n):
    points = [(x0, y0)]
    x = x0
    y = y0
    for _ in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + (h/2), y + (k1/2))
        k3 = h * f(x + (h/2), y + (k2/2))
        k4 = h * f(x + h, y + k3)
        y += ((k1 + (2*k2)) + ((2*k3) + k4)) / 6
        x += h
        points.append((x, y))
    return points

# Función para ingresar la ecuación diferencial
def get_differential_equation():
    equation = input("Ingrese la ecuación diferencial en términos de x e y (ejemplo: x**2 + math.exp(2)): ")
    return lambda x, y: eval(equation)

# Función para seleccionar el método de resolución
def select_method():
    method = input("Seleccione el método de resolución (1: Euler, 2: Euler mejorado, 3: Runge-Kutta): ")
    return method

# Función para obtener la solución exacta
def get_exacta_equation():
    equation = input("Ingrese la ecuación diferencial en términos de x e y (ejemplo: x**2 + math.exp(2)): ")
    return lambda x: eval(equation)
# Función para calcular el porcentaje de error
def calculate_error(approx, exact):
    if exact == 0:
        return "División por cero"
    else:
        return abs((exact - approx) / exact) * 100

# Función para obtener la entrada del usuario
def get_input():
    x0 = float(input("Ingrese el valor inicial de x: "))
    y0 = float(input("Ingrese el valor inicial de y: "))
    h = float(input("Ingrese el tamaño del paso (h): "))
    n = int(input("Ingrese el número de pasos (n): "))
    return x0, y0, h, n

# Función principal
def main():
    differential_eq = get_differential_equation()
    exact_solution = get_exacta_equation()
    x0, y0, h, n = get_input()
    method = select_method()
    
    if method == '1':  # Método de Euler
        solution = euler_method(differential_eq, x0, y0, h, n)
    elif method == '2':  # Método de Euler mejorado
        solution = improved_euler_method(differential_eq, x0, y0, h, n)
    elif method == '3':  # Método de Runge-Kutta
        solution = runge_kutta(differential_eq, x0, y0, h, n)
    else:
        print("Método no válido.")
        return

    print("\nResultados:")
    print("x\t\tSolución Aproximada\t\tSolución Exacta\t\tError (%)")
    for point in solution:
        exact = exact_solution(point[0])
        error = calculate_error(point[1], exact)
        print(f"{round(point[0], 5)}\t\t{round(point[1], 5)}\t\t\t{round(exact, 5)}\t\t\t{round(error, 5)}")


# Resto del código para graficar, igual que antes...
 # Preparar datos para graficar
    x_values = [point[0] for point in solution]
    y_approx_values = [point[1] for point in solution]
    y_exact_values = [exact_solution(x) for x in x_values]
    
    # Graficar las soluciones aproximadas y exactas
    plt.plot(x_values, y_approx_values, label='Solución Aproximada', color='blue')
    plt.plot(x_values, y_exact_values, label='Solución Exacta', color='red')
    
    # Configuraciones adicionales de la gráfica
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Comparación de la solución aproximada y la solución exacta')
    plt.legend()
    plt.grid(True)
    
    # Mostrar la gráfica
    plt.show()



if __name__ == "__main__":
    main()
