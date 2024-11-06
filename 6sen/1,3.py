import numpy as np
import matplotlib.pyplot as plt

# Параметры для графиков
mxs = [0, 0, 0, -1]
osqrs = [1, 3, 0.2, 1]

# Строим графики
for mx, osqr in zip(mxs, osqrs):
    # Генерируем выборку из нормального распределения
    xn = np.random.normal(mx, np.sqrt(osqr), 1000)
    # Строим гистограмму
    plt.hist(xn, bins=50, density=True, alpha=0.6, label=f'mx={mx}, o^2={osqr}')

# Устанавливаем метки осей и легенду
plt.xlabel('x')
plt.ylabel('Эмпирическая плотность распределения')
plt.legend()

# Показываем график
plt.show()
