import numpy as np
import matplotlib.pyplot as plt

duration = 1.0 # Длительность импульса в секундах
amplitude = 0.5 # Амплитуда импульса

t = np.arange(-duration / 2, duration / 2, 0.01)
triangular_pulse = amplitude * (1 - np.abs(2 * t / duration))

spectrum = np.fft.fft(triangular_pulse)
frequencies = np.fft.fftfreq(len(t))

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, triangular_pulse)
plt.title('Треугольный одиночный импульс')
plt.xlabel('Время (секунды)')
plt.ylabel('Амплитуда')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(spectrum))
plt.title('Спектр треугольного одиночного импульса')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда спектра')
plt.grid(True)

plt.tight_layout()
plt.show()