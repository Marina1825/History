import numpy as np
import matplotlib.pyplot as plt

# Параметры для графиков
mxs = [0, 0, 0, -1]
osqrs = [1, 3, 0.2, 1]

# Строим графики
for mx, osqr in zip(mxs, osqrs):
    # Генерируем точки для графика
    x = np.arange(-5, 5, 0.01)
    # Вычисляем плотность вероятности
    pdf = (1 / np.sqrt(2 * np.pi * osqr)) * np.exp(-(x - mx)**2 / (2 * osqr))
    # Строим график
    plt.plot(x, pdf, label=f'mx={mx}, o^2={osqr}')

# Устанавливаем метки осей и легенду
plt.xlabel('x')
plt.ylabel('W(x)')
plt.legend()

# Показываем график
plt.show()