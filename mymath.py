
import cmath

def quadratic_equation(a, b, c):
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    return "Корни уравнения равны: " + str(sol1)+ " и " + str(sol2)