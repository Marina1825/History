import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

f = 20 # Гц, частота сигнала
t = np.linspace(0, 0.5, 200)
x1 = np.cos(2 * np.pi * f * t)

s_rate = 40 # Частота дискретизации

T = 1 / s_rate
n = np.arange(0, 0.5 / T)
nT = n * T
x2 = np.cos(2 * np.pi * f * nT) # Since for sampling t = nT.
disc = fft(x1)

plt.figure(figsize=(10, 8))
plt.suptitle("Дискретизация синусоидального сигнала", fontsize=20)

plt.subplot(2, 2, 1)
plt.plot(t, x1, linewidth=3, label='Исходный сигнал')
plt.xlabel('Время', fontsize=15)
plt.ylabel('Амплитуда', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 2)
plt.stem(nT, x2, 'm', label='Представление сигнала в виде отсчетов')
plt.xlabel('Время', fontsize=15)
plt.ylabel('Амплитуда', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 3)
plt.plot(nT, x2, 'g-', label='Реконструируемый сигнал')
plt.xlabel('Время', fontsize=15)
plt.ylabel('Амплитуда', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 4)
plt.plot(t, disc, 'g-', label='Спектр')
plt.xlabel('Время', fontsize=15)
plt.ylabel('Амплитуда', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.tight_layout()