import numpy as np
import matplotlib.pyplot as plt

# Генерация равномерных случайных величин
t = np.linspace(0, 3, 1000)
xn1 = np.random.uniform(0, 1, len(t))
xn2 = np.random.uniform(0, 1, len(t))
xn3 = np.random.uniform(0, 1, len(t))

# Инициализация массива xn с нулями
xn = np.zeros(1000)

# Суммирование равномерных случайных величин
for i in range(1000):
    xn[i] = xn1[i] + xn2[i] + xn3[i]

# Построение гистограммы распределения xn
plt.hist(xn1, bins=30, density=True, alpha=0.6, color='g')
plt.title('Распределение xn')
plt.show()

# Генерация суммы равномерных случайных величин
M = 1000  # Количество слагаемых
Yn = np.sum(np.random.uniform(0, 1, (M, 1000)), axis=0)

# Построение гистограммы распределения Yn
plt.hist(Yn, bins=30, density=True, alpha=0.6, color='g')
plt.title('Распределение Yn')
plt.show()