import numpy as np
import matplotlib.pyplot as plt

# Функция для вычисления DFT
def compute_dft(signal):
    return np.fft.fft(signal)

# Сигналы
signals = [
    np.array([1, 1, 1, 1, 1, 1, 1, 1]),  # 1.1
    np.array([0, 0.71, 1, 0.71, 0, -0.71, -1, -0.71]),  # 1.2
    np.array([0, 1, 0, -1, 0, 1, 0, -1]),  # 1.3
    np.array([1, 1, 0, 0, 0, 0, 0, 0]),  # 1.4
    np.array([1, 1, 1, 0, 0, 0, 0, 0])  # 1.5
]

# Вычисление и построение диаграмм для каждого сигнала
for i, signal in enumerate(signals, start=1):
    # Вычисление DFT
    dft_result = compute_dft(signal)
    
    # Временная диаграмма с использованием stem
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.stem(signal, linefmt='C0', markerfmt='C0o', basefmt='C0-', use_line_collection=True)
    plt.title(f'Временная диаграмма сигнала {i} (stem)')
    
    # Спектральная диаграмма с использованием plot
    plt.subplot(2, 1, 2)
    plt.plot(np.abs(dft_result), 'C1', label='Спектр')
    plt.title(f'Спектральная диаграмма сигнала {i} (plot)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
