import numpy as np
import matplotlib.pyplot as plt

# Спектр прямоугольного импульса
xn_rect = np.array([1, 1, 0, 0, 0, 0, 0, 0])
xk_rect = np.fft.fft(xn_rect)

# Спектр треугольного импульса
xn_tri = np.array([1, 0.75, 0.5, 0.25, 0, 0, 0, 0])
xk_tri = np.fft.fft(xn_tri)

# Сигнал как сумма двух импульсов
f_n = xn_rect + xn_tri

# Спектр суммы сигналов
f_k = np.fft.fft(f_n)

# Сравнение спектров
if np.array_equal(f_k, xk_rect + xk_tri):
    print("Принцип суперпозиции подтвержден: Cf(k) = Cx(k) + Cy(k)")
else:
    print("Принцип суперпозиции не подтвержден")

# Визуализация результатов
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.stem(xk_rect.real)
plt.title('Действительная часть спектра прямоугольного импульса')

plt.subplot(2, 2, 2)
plt.stem(xk_rect.imag)
plt.title('Мнимая часть спектра прямоугольного импульса')

plt.subplot(2, 2, 3)
plt.stem(xk_tri.real)
plt.title('Действительная часть спектра треугольного импульса')

plt.subplot(2, 2, 4)
plt.stem(xk_tri.imag)
plt.title('Мнимая часть спектра треугольного импульса')

plt.tight_layout()
plt.show()