import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

fs = 100
ts = 1/fs
t = np.arange(0, 1, 0.01)
cs = np.cos(2 * np.pi * 10 * t)
snr_db = 4  # требуемое отношение сигнал/шум
cs2 = cs ** 2
sig_awg_watts = np.mean(cs2)
sig_awg_db = 10 * np.log10(sig_awg_watts)
noise_awg_db = sig_awg_db - snr_db
noise_awg_watts = 10 ** (noise_awg_db / 10) 
mean_noise = 0

noise_volts = np.random.normal(mean_noise, np.sqrt(noise_awg_watts), len(cs))
cs_n = cs + noise_volts

# Вычисление корреляционного интеграла
sr = ts * np.sum(cs_n * cs)

# Функция для вычисления вероятности ошибки
def Q(x):
    return 0.5 * erfc(x / np.sqrt(2))

# Вычисление вероятности ошибки приема символа ДАМ
Ps_dqpsk = Q(np.sqrt(2 * (10 ** (0.1 * snr_db))))

# Вычисление вероятности ошибки приема символа ДФМ
Ps_dfm = Q(np.sqrt(10 ** (0.1 * snr_db)))

# График BER строится в зависимости от отношения сигнал/шум в дБ
snr_db_range = np.arange(0, 15, 0.1)
ber_dam = [Q(np.sqrt(2 * (10 ** (0.1 * snr)))) for snr in snr_db_range]
ber_dfm = [Q(np.sqrt(10 ** (0.1 * snr))) for snr in snr_db_range]

snr_db_range = np.arange(0, 15, 0.1)
ber_dam = [Q(np.sqrt(2 * (10 ** (0.1 * snr)))) for snr in snr_db_range]
ber_dfm = [Q(np.sqrt(10 ** (0.1 * snr))) for snr in snr_db_range]

# Создание графика
plt.figure(figsize=(10, 6))

# Добавление сетки
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Добавление линий графика
plt.semilogy(snr_db_range, ber_dam, label='DQPSK')
plt.semilogy(snr_db_range, ber_dfm, label='DFM')


# Настройка осей
plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.title('Bit Error Rate (BER) vs SNR')
plt.legend()

