import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

Ts1 = 2e-3 # интервал дискретизации
fs1 = 1 / Ts1
f0 = (0.4 * np.pi * fs1) / (2 * np.pi) # аналоговая частота
t = np.arange(-5, 11) * Ts1

for f in range(25, 226, 50):
s = np.cos(f * t * (2 * np.pi))
sp = fftpack.fft(s)
freqs = np.fft.fftfreq(len(s), d=Ts1)
fig, ax = plt.subplots()
ax.stem(freqs, np.abs(sp))
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Magnitude')
ax.set_title(f'Spectrum of Signal with Frequency {f} Hz')
ax.grid()
plt.show()