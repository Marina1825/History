import numpy as np
from scipy import integrate

def W(xn, m, osqr):
    return (1 / np.sqrt(2 * np.pi * osqr)) * np.exp(-(xn - m)**2 / (2 * osqr))

def integrand_m(xn, m, osqr):
    return xn * W(xn, m, osqr)

def integrand_o(xn, m, osqr):
    return xn**2 * W(xn, m, osqr)

# Параметры для графиков
ms = [0, 0, 0, -1]
osqrs = [1, 3, 0.2, 1]

a = -np.inf  # Нижняя граница интегрирования
b = np.inf

for m, osqr in zip(ms, osqrs):
    xn = np.random.normal(m, np.sqrt(osqr), 1000)
    # Вычисление интеграла с помощью integrate.quad
    result_m, error = integrate.quad(integrand_m, a, b, args=(m, osqr))
    
    mx = result_m
    
    result_o, error = integrate.quad(integrand_o, a, b, args=(m, osqr))
    
    osq = result_o  - mx**2
    print(f"Для m = {m} и osqr = {osqr}, mx = {mx}, osqr = {osq}")
    