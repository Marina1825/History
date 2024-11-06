import numpy as np
import matplotlib.pyplot as plt

%matplotlib

def generate_analog_signal(A, frequency, T, size):
    t = np.linspace(0, (size-1)*T, size)
    x = A * np.cos(2 * np.pi * frequency * t)
    return x

A = 1       # Амплитуда
f = 5       # Частота сигнала, Гц
fs = 100    # Частота дискретизации, отсч/сек
T = 1/fs    # Интервал времени

sizes = [64, 128, 256]

for size in sizes:
    x = generate_analog_signal(A, f, T, size)
    X = np.fft.fft(x)
    freq = np.fft.fftfreq(size, d=T)
    plt.plot(freq, np.abs(X))
    plt.xlabel('Частота, Гц')
    plt.ylabel('Модуль спектра')
    plt.show()
