import numpy as np
import funct as func
from scipy.fft import fftshift, fft
import matplotlib.pyplot as plt
%matplotlib

def add_CRC(kod, M):
    delet = [1, 1, 1, 1, 1, 0, 1, 1]
    
    for i in range(len(delet) - 1):
        kod.append(0)
    
    CRCnum = func.CRC(kod)
    
    for i in range(M, len(kod)):
        kod[i] = CRCnum[i - M]
    
    return kod

def generate_signal(kod, G, N, key):
    golden, _ = func.Gold()
    
    for i in range(G):
        kod.append(0)
        kod = func.shiftright(kod)  
    
    for i in range(G):
        kod[i] = golden[i]
    
    signal = np.repeat(kod, N)
    
    bigsignal = np.zeros(2 * len(signal), dtype=int)
    
    for i in range(len(bigsignal)):
        if key <= i < key + len(signal):
            bigsignal[i] = signal[i - key]
    
    return bigsignal

def add_noise(signal, o):
    noise = np.random.normal(0, o, len(signal))
    signoise = noise + signal
    return signoise

def calculate_spectrum(signoise):
    signal_part = signoise[110:500]
    spectrum = fftshift(fft(signal_part))
    return spectrum

def main(N, key, o):
    name = "Buyanova Marina"
    kod = func.coder(name)
    M = len(kod)
    
    kod = add_CRC(kod, M)
    
    signal = generate_signal(kod, func.Gold()[1], N, key)
    
    signoise = add_noise(signal, o)
    
    spectrum = calculate_spectrum(signoise)
    
    return spectrum

if __name__ == "__main__":
    rec_spectrum = main(2, 120, 0.15)
    man_spectrum = main(4, 120, 0.15)
    dig_spectrum = main(8, 120, 0.15)
    
    plt.figure()
    plt.xlabel("Частота")
    plt.ylabel("Амплитуда")
    plt.title("Спектры сигналов")
    plt.plot(rec_spectrum, "g")
    plt.plot(man_spectrum, "r")
    plt.plot(dig_spectrum, "b")
    plt.show()
