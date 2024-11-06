import numpy as np
import matplotlib.pyplot as plt

# Параметры сигнала
symbol = "Buyanova"
sampling_rate = 8000  # Частота дискретизации (в Гц)
symbol_duration = 0.1  # Длительность символа (в секундах)
samples_per_symbol = int(sampling_rate * symbol_duration)

# Функция для формирования сигнала ДАМ
def dam_signal(symbol, samples_per_symbol):
    signal = np.zeros(len(symbol) * samples_per_symbol)
    for i, char in enumerate(symbol):
        start = i * samples_per_symbol
        end = start + samples_per_symbol
        signal[start:end] = np.ones(samples_per_symbol) if char.isupper() else np.zeros(samples_per_symbol)
    return signal

# Функция для формирования сигнала ДФМ
def dfm_signal(symbol, samples_per_symbol, sampling_rate):
    signal = np.zeros(len(symbol) * samples_per_symbol)
    for i, char in enumerate(symbol):
        start = i * samples_per_symbol
        end = start + samples_per_symbol
        freq = (ord(char) - ord('A') + 1) * 100  # Примерная частота для символа
        t = np.linspace(0, symbol_duration, samples_per_symbol, endpoint=False)
        signal[start:end] = np.sin(2 * np.pi * freq * t)
    return signal

# Формирование сигналов ДАМ и ДФМ
dam_sig = dam_signal(symbol, samples_per_symbol)
dfm_sig = dfm_signal(symbol, samples_per_symbol, sampling_rate)

# Отображение сигналов на графиках
plt.figure(figsize=(14, 7))

# График сигнала ДАМ
plt.subplot(2, 1, 1)
plt.plot(dam_sig)
plt.title('Сигнал ДАМ для символа "Buyanova"')
plt.xlabel('Отсчеты')
plt.ylabel('Амплитуда')

# График сигнала ДФМ
plt.subplot(2, 1, 2)
plt.plot(dfm_sig)
plt.title('Сигнал ДФМ для символа "Buyanova"')
plt.xlabel('Отсчеты')
plt.ylabel('Амплитуда')

# Отображение графиков
plt.tight_layout()
plt.show()
