import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 2000)

f = 40 *4 
amplitude = 3  
phase = np.pi / 7 

signal = amplitude * np.cos(2 * np.pi * f * t + phase)

signal_fft = np.fft.fft(signal)

frequencies = np.fft.fftfreq(len(signal), t[1] - t[0])

spectrum = np.abs(signal_fft)

max_freq_index = np.argmax(spectrum)

# Находим максимальную частоту
max_frequency = frequencies[max_freq_index]

print("Максимальная частота в спектре сигнала:", max_frequency)

fs_min = 2 * f

print("Минимальная необходимая частота дискретизации (теорема Котельникова):", fs_min)

fs_min = 2 * f

fs = fs_min

num_samples = int(1 * fs)

digitized_signal = signal[:num_samples]

dft_result = np.fft.fft(digitized_signal)


threshold = 0.1
significant_frequencies = np.where(np.abs(dft_result) > threshold)[0]
spectrum_width = max(significant_frequencies) - min(significant_frequencies)

memory_size_bytes = dft_result.nbytes

reconstructed_signal = np.fft.ifft(dft_result)

print("Ширина спектра:", spectrum_width)
print("Объем памяти, требуемый для хранения массива dft_result (в байтах):", memory_size_bytes)

plt.figure(figsize=(8, 4))
plt.plot(t[:num_samples], digitized_signal, label='Оцифрованный сигнал', linestyle='--')
plt.plot(t[:num_samples], reconstructed_signal, label='Восстановленный сигнал', linestyle='-')
plt.title('Восстановление оригинального сигнала')
plt.xlabel('Время (секунды)')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid(True)
plt.show()