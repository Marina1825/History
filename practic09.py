import matplotlib.pyplot as plt
import random
import numpy as np

# Шаг 1: Сгенерировать 1000 случайных бит
random_bits = ''.join(random.choice('01') for _ in range(10000))

# Шаг 2: Разделить биты на группы по 4
binary_numbers = [random_bits[i:i+4] for i in range(0, len(random_bits), 4)]

# Шаг 3: Преобразовать двоичные числа в комплексный вид для QAM-16 с использованием кода Грея
def binary_to_gray(binary):
    return binary[0] + str(int(binary[1]) ^ int(binary[0])) + str(int(binary[2]) ^ int(binary[3])) + str(int(binary[3]))

def binary_to_qam16(binary):
    gray_code = binary_to_gray(binary)
    amplitude_map = {'00': -3, '01': -1, '10': 1, '11': 3}
    real_part = amplitude_map[gray_code[0:2]]
    imag_part = amplitude_map[gray_code[2:4]]
    return complex(real_part, imag_part)

qam16_numbers = [binary_to_qam16(binary) for binary in binary_numbers]

# Шаг 4: Добавить шум к сигналу
def add_awgn_noise(signal, snr_db):
    snr = 10**(snr_db / 10)
    signal_power = np.mean(np.abs(signal)**2)
    noise_power = signal_power / snr
    noise = np.sqrt(noise_power / 2) * (np.random.randn(len(signal)) + 1j * np.random.randn(len(signal)))    
    return signal + noise, noise

# Выберем SNR в дБ (например, 10 дБ)
snr_db = 12
noisy_qam16_numbers, noise = add_awgn_noise(qam16_numbers, snr_db)

# Шаг 5: Нарисовать созвездие
plt.figure(figsize=(6, 6))

# Отображение идеальных точек созвездия
ideal_points = [binary_to_qam16(binary_to_gray(bin(i)[2:].zfill(4))) for i in range(16)]
plt.scatter([c.real for c in ideal_points], [c.imag for c in ideal_points], s=100, c='red', marker='x')

# Отображение точек с шумом
plt.scatter([c.real for c in noisy_qam16_numbers], [c.imag for c in noisy_qam16_numbers], s=50, c='blue')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Constellation Diagram for QAM-16 with AWGN (SNR = {} dB)'.format(snr_db))
plt.show()

# Шаг 6: Декодирование сигнала с использованием кода Грея
def gray_to_binary(gray):
    binary = gray[0]
    binary += str(int(binary[-1]) ^ int(gray[1]))
    binary += str(int(binary[-1]) ^ int(gray[2]))
    binary += str(int(binary[-1]) ^ int(gray[3]))
    return binary

def qam16_to_binary(qam16):
    amplitude_map = {(-3, -3): '0000', (-3, -1): '0001', (-3, 1): '0011', (-3, 3): '0010',
                     (-1, -3): '0100', (-1, -1): '0101', (-1, 1): '0111', (-1, 3): '0110',
                     (1, -3): '1100', (1, -1): '1101', (1, 1): '1111', (1, 3): '1110',
                     (3, -3): '1000', (3, -1): '1001', (3, 1): '1011', (3, 3): '1010'}
    real_part = qam16.real
    imag_part = qam16.imag
    if (real_part <= -2):
        real_part = -3
    if (-2 < real_part < 0):
        real_part = -1
    if (0 <= real_part < 2):
        real_part = 1
    if (2 <= real_part):
        real_part = 3
    if (imag_part <= -2):
        imag_part = -3
    if (-2 < imag_part < 0):
        imag_part = -1
    if (0 <= imag_part < 2):
        imag_part = 1
    if (2 <= imag_part):
        imag_part = 3
    gray_code = amplitude_map[(real_part, imag_part)]
    return gray_to_binary(gray_code)

decoded_bits = ''.join(qam16_to_binary(qam16) for qam16 in noisy_qam16_numbers)

# Шаг 7: Анализ ошибок
errors = sum(1 for a, b in zip(random_bits, decoded_bits) if a != b)
ber = errors / len(random_bits)
print(f"Bit Error Rate (BER): {ber:.6f}")