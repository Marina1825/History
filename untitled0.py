import numpy as np
import matplotlib.pyplot as plt

# Параметры
c = 10**8
f = 2.5 * 10**9
lam = c / f
d = 0.5 * lam
N_4 = 4
N_8 = 8

def array_response_vector(array, phi, d, lam):
    v = np.exp(1j * 2 * np.pi * array * d / lam * np.sin(phi))
    return v

# Углы
phi = np.linspace(-np.pi, np.pi, 360)

# Расчет AF для решетки из 4 элементов
array_4 = np.arange(0, N_4)
Ar_4 = np.zeros((N_4, phi.size), dtype=complex)
for j in range(phi.size):
    Ar_4[:, j] = array_response_vector(array_4, phi[j], d, lam)

AF_4 = np.sum(Ar_4, axis=0)
AF_4_abs = np.abs(AF_4)**2

# Расчет AF для решетки из 8 элементов
array_8 = np.arange(0, N_8)
Ar_8 = np.zeros((N_8, phi.size), dtype=complex)
for j in range(phi.size):
    Ar_8[:, j] = array_response_vector(array_8, phi[j], d, lam)

AF_8 = np.sum(Ar_8, axis=0)
AF_8_abs = np.abs(AF_8)**2

# Построение ДН для решеток 4 и 8 элементов
plt.figure(1)
plt.polar(phi, AF_4_abs, label='N=4')
plt.polar(phi, AF_8_abs, label='N=8')
plt.legend()
plt.title('Диаграмма направленности для N=4 и N=8')

# Поворот ДН на заданный угол
teta0 = 45 * np.pi / 180  # Угол поворота
delta = -(2 * np.pi * d / lam) * np.sin(teta0)

# Расширение фазового сдвига для каждого элемента и каждого угла
delta_expanded_4 = np.exp(1j * array_4[:, np.newaxis] * delta)
delta_expanded_8 = np.exp(1j * array_8[:, np.newaxis] * delta)

# Повернутая ДН для решетки из 4 элементов
AF_4_rotated = np.sum(Ar_4 * delta_expanded_4, axis=0)
AF_4_rotated_abs = np.abs(AF_4_rotated)**2

# Повернутая ДН для решетки из 8 элементов
AF_8_rotated = np.sum(Ar_8 * delta_expanded_8, axis=0)
AF_8_rotated_abs = np.abs(AF_8_rotated)**2

# Построение повернутых ДН
plt.figure(2)
plt.polar(phi, AF_4_rotated_abs, label='N=4 (rotated)')
plt.polar(phi, AF_8_rotated_abs, label='N=8 (rotated)')
plt.legend()
plt.title('Повернутая диаграмма направленности для N=4 и N=8')

plt.show()