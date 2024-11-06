import numpy as np
import matplotlib.pyplot as plt

# Параметры распределения
m = 0  # матожидание
s1 = 1  # дисперсия

# Генерация реализаций СВ
t = np.linspace(0, 3, 100)
xn = np.random.normal(m, s1, len(t))

# Преобразование реализаций СВ
xn1 = np.convolve(xn, [1, 0.7, 0.3, 0.1, 0.05])
index = np.random.randint(0, len(t))
section = [0] * len(index)  # Инициализация списка нужного размера
for i, index in enumerate(index):
    
    section[i] = xn1[index]

# Временная диаграмма реализации СВ
plt.figure(figsize=(10, 5))
plt.plot(t, xn1[:len(t)])  # Используем только первые len(t) элементов xn1
plt.title('Time diagram of the realization of the random process')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()

# Гистограмма распределения значений СВ в сечении t0
plt.figure(figsize=(10, 5))
plt.hist(section, bins=30, density=True)
plt.title('Histogram of the values of the random process in the section')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Генерация большого количества реализаций и вычисление АКФ
tau_values = [0, 3, 5, 7]
B_values = []

for tau in tau_values:
    B_tau = 0
    for _ in range(1000):  # большое количество реализаций
        xn = np.random.normal(m, s1, len(t))
        xn1 = np.convolve(xn, [1, 0.7, 0.3, 0.1, 0.05])
        index1 = np.random.randint(0, len(t))
        index2 = index1 + tau
        # Проверяем, что индекс не выходит за пределы массива xn1
        if index2 < len(xn1):
            B_tau += xn1[index1] * xn1[index2]
    B_tau /= 1000
    B_values.append(B_tau)

# Вычисление АКФ
B0 = B_values[0]
T0 = (1 / B0) * np.trapz(B_values, tau_values)

# График АКФ
plt.figure(figsize=(10, 5))
plt.plot(tau_values, B_values)
plt.title('Autocorrelation function')
plt.xlabel('tau')
plt.ylabel('B(tau)')
plt.show()

print(f'Interval of correlation: {T0}')