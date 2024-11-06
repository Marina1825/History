import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Параметры для графиков
osqrs = [1, 3, 0.2, 1]
m = 0
t = np.linspace(0, 3, 1000)

# Строим графики
plt.figure(figsize=(10, 10))

for osqr, s1 in zip(osqrs, [np.sqrt(o) for o in osqrs]):
    # Генерируем выборку
    xn = np.random.normal(m, s1, len(t))
    # Строим график выборки
    plt.subplot(2, 2, 1)
    plt.hist(xn, bins=30, density=True, alpha=0.6, label='Выборка')
    plt.xlabel('x')
    plt.ylabel('Частота')
    plt.legend()
    # Строим график плотности распределения
    plt.subplot(2, 2, 2)
    plt.plot(t, norm.pdf(t, m, s1), label='Плотность распределения')
    plt.xlabel('x')
    plt.ylabel('W(x)')
    plt.legend()
    # Строим график значений СВ
    plt.subplot(2, 2, 3)
    plt.plot(t, xn, label='значений СВ')
    plt.xlabel('xn')
    plt.ylabel('W(x)')
    plt.legend()

# Показываем графики
plt.tight_layout()
plt.show()