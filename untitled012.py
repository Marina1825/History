import numpy as np
import matplotlib.pyplot as plt

duration = 1.0  # Длительность импульса в секундах
amplitude = 1.0  # Амплитуда импульса

t = np.linspace(-duration / 2, duration / 2, 1000)
triangular_pulse = amplitude * (1 - np.abs(2 * t / duration))

spectrum = np.fft.fft(triangular_pulse)
frequencies = np.fft.fftfreq(len(t), t[1] - t[0])

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, triangular_pulse)
plt.title('Треугольный импульс')
plt.xlabel('Время (секунды)')
plt.ylabel('Амплитуда')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(spectrum))
plt.title('Спектр треугольного импульса')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда спектра')
plt.grid(True)

plt.tight_layout()
plt.show()