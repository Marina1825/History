import numpy as np
import matplotlib.pyplot as plt

%matplotlib

def generate_analog_signal(A, frequency, T, size):
    t = np.linspace(0, (size-1)*T, size)
    x = A * np.cos(2 * np.pi * frequency * t)
    return x

A = 1       # Амплитуда
f = 5       # Частота сигнала, Гц
fs = 50     # Частота дискретизации, отсч/сек
T = 1/fs    # Интервал времени

sizes = [64, 128, 256]

for size in sizes:
    x = generate_analog_signal(A, f, T, size)
    n = np.arange(size)
    plt.plot(n, x)
    plt.xlabel('Отсчеты')
    plt.ylabel('Амплитуда')
    plt.show()

normalized_frequency = 0.1 * np.pi
fs = 50

analog_frequency = normalized_frequency * fs / (2 * np.pi)
print("Аналоговая частота для нормированной частоты 0.1π рад: ", analog_frequency)

normalized_frequency = 0.3 * np.pi
fs = 50

analog_frequency = normalized_frequency * fs / (2 * np.pi)
print("Аналоговая частота для нормированной частоты 0.3π рад: ", analog_frequency)

