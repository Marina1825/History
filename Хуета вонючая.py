from scipy.fftpack import fft, ifft, fftshift
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Задание 1
# Параметры сигнала
fs = 100  # частота дискретизации
t = np.arange(0, 1, 1/fs)  # временной вектор
fc = 10   # Частота несущей

# Генерация синфазной и квадратурной компонент
amplitudes = np.array([1, -1, 3, -3])
np.random.shuffle(amplitudes)
A_I = amplitudes[0]
A_Q = amplitudes[1]

I = A_I * np.cos(2 * np.pi * fc * t)
Q = A_Q * np.sin(2 * np.pi * fc * t)

qam_signal = I + Q

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, qam_signal, label='QAM Signal')
plt.title("Временная диаграмма КАМ сигнала")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.legend()

qam_spectrum = fft(qam_signal)
freq = np.linspace(-fs/2, fs/2, len(qam_spectrum))

plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(fftshift(qam_spectrum)), label='Spectrum of QAM Signal')
plt.title("Спектральная диаграмма КАМ сигнала")
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплитуда")
plt.legend()

plt.tight_layout()
plt.show()

# Задание 2
# Параметры сигнала
fs = 100  # частота дискретизации
t = np.arange(0, 1, 1/fs)  # временной вектор
fc = 10   # Частота несущей

# Генерация синфазной и квадратурной компонент
I = np.cos(2 * np.pi * fc * t)
Q = np.sin(2 * np.pi * fc * t)
qam_signal = I + Q

# Генерация шума с разными значениями SNR
snr_values = [20, 10, 0, -10]  # dB
plt.figure(figsize=(12, 6))

for snr in snr_values:
    # Мощность сигнала
    signal_power = np.mean(qam_signal ** 2)
    # Мощность шума
    noise_power = signal_power / (10 ** (snr / 10))
    # Генерация шума
    noise = np.random.normal(0, np.sqrt(noise_power), len(qam_signal))
    # Суммарный сигнал
    noisy_signal = qam_signal + noise

    plt.plot(t, noisy_signal, label=f'SNR={snr} dB')

plt.title("Временные диаграммы сигналов с разным SNR")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.legend()
plt.show()

# Задание 3
fs = 100  # частота дискретизации
t = np.arange(0, 1, 1/fs)  # временной вектор
fc = 10   # Частота несущей
snr = 10  # Желаемое отношение сигнал/шум в дБ

# Генерация синфазной и квадратурной компонент
I = np.cos(2 * np.pi * fc * t)
Q = np.sin(2 * np.pi * fc * t)
qam_signal = I + Q

# Генерация шума
signal_power = np.mean(qam_signal ** 2)
noise_power = signal_power / (10 ** (snr / 10))
noise = np.random.normal(0, np.sqrt(noise_power), len(qam_signal))
received_signal = qam_signal + noise

# Визуализация принятого сигнала и его спектра
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, received_signal)
plt.title("Принятый сигнал")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")

received_spectrum = fft(received_signal)
freq = np.linspace(-fs/2, fs/2, len(received_spectrum))

plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(fftshift(received_spectrum)))
plt.title("Спектр принятого сигнала")
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплитуда")

# Проектирование фильтра и его АЧХ
n = 61
taps = signal.firwin(n, 0.1, fs=fs)
w, h = signal.freqz(taps, worN=8000, fs=fs)

plt.figure()
plt.plot(w, np.abs(h))
plt.title('Амплитудно-частотная характеристика фильтра')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()
    
# Задание 4
fs = 100  # частота дискретизации
t = np.arange(0, 1, 1/fs)  # временной вектор
fc = 10   # Частота несущей
snr = 10  # Желаемое отношение сигнал/шум в дБ

# Генерация синфазной и квадратурной компонент
I = np.cos(2 * np.pi * fc * t)
Q = np.sin(2 * np.pi * fc * t)
qam_signal = I + Q

# Генерация шума
signal_power = np.mean(qam_signal ** 2)
noise_power = signal_power / (10 ** (snr / 10))
noise = np.random.normal(0, np.sqrt(noise_power), len(qam_signal))
received_signal = qam_signal + noise

# Проектирование фильтра
n = 61
taps = signal.firwin(n, 0.1, fs=fs)

# Фильтрация сигналов в каждом канале
filtered_I = signal.lfilter(taps, 1.0, received_signal * I)
filtered_Q = signal.lfilter(taps, 1.0, received_signal * Q)

# Временная диаграмма и спектр фильтрованных сигналов
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, filtered_I, label='Filtered I Channel')
plt.plot(t, filtered_Q, label='Filtered Q Channel')
plt.title("Сигналы на выходе фильтра")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.legend()

# Спектры фильтрованных сигналов
FI_spectrum = fft(filtered_I)
FQ_spectrum = fft(filtered_Q)
freq = np.linspace(-fs/2, fs/2, len(FI_spectrum))

plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(fftshift(FI_spectrum)), label='Spectrum of Filtered I')
plt.plot(freq, np.abs(fftshift(FQ_spectrum)), label='Spectrum of Filtered Q')
plt.title("Спектры фильтрованных сигналов")
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплитуда")
plt.legend()
plt.tight_layout()
plt.show()

# Задание 5
fs = 100  # частота дискретизации
t = np.arange(0, 1, 1/fs)  # временной вектор
fc = 10   # Частота несущей
snr = 10  # Желаемое отношение сигнал/шум в дБ

# Генерация сигнала КАМ
I = np.cos(2 * np.pi * fc * t)
Q = np.sin(2 * np.pi * fc * t)
qam_signal = I + Q

# Смещение частоты для опорного колебания
frequency_offset = 0.1  # смещение частоты на 0.1 Гц
I_offset = np.cos(2 * np.pi * (fc + frequency_offset) * t)
Q_offset = np.sin(2 * np.pi * (fc + frequency_offset) * t)

# Генерация шума и получение сигнала на приемнике
signal_power = np.mean(qam_signal ** 2)
noise_power = signal_power / (10 ** (snr / 10))
noise = np.random.normal(0, np.sqrt(noise_power), len(qam_signal))
received_signal = qam_signal + noise

# Демодуляция с смещением частоты
received_I = received_signal * I_offset
received_Q = received_signal * Q_offset

# Фильтрация демодулированных сигналов
n = 61
taps = signal.firwin(n, 0.1, fs=fs)
filtered_I = signal.lfilter(taps, 1.0, received_I)
filtered_Q = signal.lfilter(taps, 1.0, received_Q)

# Визуализация демодулированных сигналов
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, filtered_I, label='Filtered I with frequency offset')
plt.plot(t, filtered_Q, label='Filtered Q with frequency offset')
plt.title("Сигналы на выходе фильтра с частотным смещением")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.legend()

# Спектр демодулированных сигналов
FI_spectrum = fft(filtered_I)
FQ_spectrum = fft(filtered_Q)
freq = np.linspace(-fs/2, fs/2, len(FI_spectrum))

plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(fftshift(FI_spectrum)), label='Spectrum of Filtered I with offset')
plt.plot(freq, np.abs(fftshift(FQ_spectrum)), label='Spectrum of Filtered Q with offset')
plt.title("Спектры демодулированных сигналов с частотным смещением")
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплитуда")
plt.legend()
plt.tight_layout()
plt.show()

# Заданиие 6
fs = 100  # частота дискретизации
t = np.arange(0, 1, 1/fs)  # временной вектор
fc = 10   # Частота несущей
snr = 10  # Желаемое отношение сигнал/шум в дБ

# Генерация сигнала КАМ
I = np.cos(2 * np.pi * fc * t)
Q = np.sin(2 * np.pi * fc * t)
qam_signal = I + Q

# Генерация шума
signal_power = np.mean(qam_signal ** 2)
noise_power = signal_power / (10 ** (snr / 10))
noise = np.random.normal(0, np.sqrt(noise_power), len(qam_signal))
received_signal = qam_signal + noise

# Амплитудное смещение для опорных колебаний
amplitude_offset = 0.1  # Смещение амплитуды на 10%
I_offset = (1 + amplitude_offset) * np.cos(2 * np.pi * fc * t)
Q_offset = (1 - amplitude_offset) * np.sin(2 * np.pi * fc * t)

# Демодуляция с амплитудным смещением
received_I = received_signal * I_offset
received_Q = received_signal * Q_offset

# Фильтрация демодулированных сигналов
n = 61
taps = signal.firwin(n, 0.1, fs=fs)
filtered_I = signal.lfilter(taps, 1.0, received_I)
filtered_Q = signal.lfilter(taps, 1.0, received_Q)

# Визуализация демодулированных и фильтрованных сигналов
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, filtered_I, label='Filtered I with amplitude offset')
plt.plot(t, filtered_Q, label='Filtered Q with amplitude offset')
plt.title("Сигналы на выходе фильтра с амплитудным смещением")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.legend()

# Спектры фильтрованных сигналов
FI_spectrum = fft(filtered_I)
FQ_spectrum = fft(filtered_Q)
freq = np.linspace(-fs/2, fs/2, len(FI_spectrum))

plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(fftshift(FI_spectrum)), label='Spectrum of Filtered I with amplitude offset')
plt.plot(freq, np.abs(fftshift(FQ_spectrum)), label='Spectrum of Filtered Q with amplitude offset')
plt.title("Спектры демодулированных сигналов с амплитудным смещением")
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплитуда")
plt.legend()
plt.tight_layout()
plt.show()

# Задание 7
fs = 100  # частота дискретизации
t = np.arange(0, 1, 1/fs)  # временной вектор
fc = 10   # Частота несущей
snr = 10  # Желаемое отношение сигнал/шум в дБ
phase_offset = np.pi / 4  # Фазовое смещение в радианах

# Генерация сигнала КАМ
I = np.cos(2 * np.pi * fc * t)
Q = np.sin(2 * np.pi * fc * t)
qam_signal = I + Q

# Генерация шума
signal_power = np.mean(qam_signal ** 2)
noise_power = signal_power / (10 ** (snr / 10))
noise = np.random.normal(0, np.sqrt(noise_power), len(qam_signal))
received_signal = qam_signal + noise

# Фазовое смещение для опорных колебаний
I_offset = np.cos(2 * np.pi * fc * t + phase_offset)
Q_offset = np.sin(2 * np.pi * fc * t + phase_offset)

# Демодуляция с фазовым смещением
received_I = received_signal * I_offset
received_Q = received_signal * Q_offset

# Фильтрация демодулированных сигналов
n = 61
taps = signal.firwin(n, 0.1, fs=fs)
filtered_I = signal.lfilter(taps, 1.0, received_I)
filtered_Q = signal.lfilter(taps, 1.0, received_Q)

# Визуализация демодулированных и фильтрованных сигналов
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, filtered_I, label='Filtered I with phase offset')
plt.plot(t, filtered_Q, label='Filtered Q with phase offset')
plt.title("Сигналы на выходе фильтра с фазовым смещением")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.legend()

# Спектры фильтрованных сигналов
FI_spectrum = fft(filtered_I)
FQ_spectrum = fft(filtered_Q)
freq = np.linspace(-fs/2, fs/2, len(FI_spectrum))

plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(fftshift(FI_spectrum)), label='Spectrum of Filtered I with phase offset')
plt.plot(freq, np.abs(fftshift(FQ_spectrum)), label='Spectrum of Filtered Q with phase offset')
plt.title("Спектры демодулированных сигналов с фазовым смещением")
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплитуда")
plt.legend()
plt.tight_layout()
plt.show()

# Вызов функций для выполнения подзаданий
task5()
task6()
task7()
task8()
task9()
task10()
task11()
