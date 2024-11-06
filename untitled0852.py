import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import kaiserord, lfilter, firwin, freqz
from scipy import fftpack
from scipy.signal import firwin, freqz
import matplotlib.pyplot as plt

f1= 1800 # выбрать частоту 
f2= 860 #выбрать частоту 
fs=7200
Ts = 1/fs
t = np.arange(0, 100)*Ts
s =  np.cos(f1*t*(2*np.pi)) + np.cos(f2*t*(2*np.pi))

Wn = f1 / (fs / 2)  # Нормированная частота среза
print("Нормированная частота среза F1:", Wn)

# Расчет коэффициентов ИХ
n = 15  # Количество отсчетов
h = firwin(n, Wn)  # Расчет коэффициентов ИХ
print("Коэффициенты ИХ:", h)

plt.figure(1)
sp = fftpack.fft(s)

freqs=np.arange(0,fs,fs/len(s))


plt.plot(freqs, np.abs(sp))
plt.xlabel('Частота в герцах [Hz]')
plt.ylabel('Модуль спектра')

fc =  4300
wc = fc*2*np.pi/fs
M = 44
n=np.arange(-M,M+1) 

h=-(np.sin(wc*n)/(np.pi*n))
h[M]=wc/np.pi
plt.figure(2) #Импульсная характеристика фильтра h(n)
plt.stem(h)
plt.xlabel('Импульсная характеристика фильтра h(n)')

plt.figure(3)
w, hf = freqz(h, fs, whole=True) #Частотная  характеристика фильтра H(jw)
plt.plot(w,20*np.log(np.abs(hf))) 
plt.xlabel(' Частотная  характеристика фильтра H(jw)')


y=np.convolve(s,h) # Вычисление сигнала на выходе фильтра через свертку 

plt.figure(4)
yf = fftpack.fft(y)

freqs=np.arange(0,fs,fs/len(yf))
plt.plot(freqs, np.abs(yf))
plt.xlabel('Частота в герцах [Hz]')
plt.ylabel('Модуль спектра сигнала на выходе фильтра')