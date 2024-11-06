import numpy as np
import random
import matplotlib.pyplot as plt
from modul import helper_func
from scipy.linalg import toeplitz


def randomDataGenerator(size):
	data = [random.randint(0, 1) for i in range(size)]
	return data

array_bit = randomDataGenerator(100000)

snr = np.arange(0,30,1)

def code_Grey_16(b):
    mass_grey = []
    for i in range(0,len(b),4):
        g1 = b[i]
        g2 = b[i+1] ^ b[i]
        g3 = b[i+2] ^ b[i+1]
        g4 = b[i+3] ^ b[i+2]
        mass_grey.append(g1)
        mass_grey.append(g2)
        mass_grey.append(g3)
        mass_grey.append(g4)
    return np.asarray(mass_grey) 

mass_code_grey_orig = code_Grey_16(array_bit)

def mapping(bit):
    imag = []
    real = []
    for i in range(0,len(bit),4):
        # print(bit[i+2], bit[i+3])
        if bit[i] == 0 and bit[i+1] == 0:
            real.append(-3)
        if bit[i] == 0 and bit[i+1] == 1:
            real.append(-1)
        if bit[i] == 1 and bit[i+1] == 1:
            real.append(1)
        if bit[i] == 1 and bit[i+1] == 0:
            real.append(3)
        if bit[i+2] == 0 and bit[i+3] == 0:
            imag.append(-3)
        if bit[i+2] == 0 and bit[i+3] == 1:
            imag.append(-1)
        if bit[i+2] == 1 and bit[i+3] == 1:
            imag.append(1)
        if bit[i+2] == 1 and bit[i+3] == 0:
            imag.append(3) 
    complex_numbers = [complex(r, i) for r, i in zip(real, imag)]
    return np.asarray(complex_numbers)

samples = mapping(mass_code_grey_orig)

h3 = np.array([0.2, 0.9, 0.3])

def SER(samples, orig_sample):
    def identify_qam16_point(sample):
        real = sample.real
        imag = sample.imag
        # Определение реальной части
        if real > 2:
            real_level = 3
        elif real > 0:
            real_level = 1
        elif real > -2:
            real_level = -1
        else:
            real_level = -3
        # Определение мнимой части
        if imag > 2:
            imag_level = 3
        elif imag > 0:
            imag_level = 1
        elif imag > -2:
            imag_level = -1
        else:
            imag_level = -3
        return complex(real_level, imag_level)

    # Применяем функцию ко всем семплам и возвращаем результат
    results = []
    for sample in samples:
        point = identify_qam16_point(sample)
        #print(type(point))
        results.append(point)
    error = 0

    
    for i in range(len(samples)):
        if abs(results[i] - orig_sample[i])!=0:
            
            error+=1
            
    ser = error/len(samples)
    
    return ser

#def ser_channel(samples, snr, h3):
ser_n_mass = []
ser_ch_mass = []
for i in range(len(snr)):
    sig = helper_func.sigma(snr[i],samples)
    noise = np.random.normal(0, sig, len(samples)) + 1j * np.random.normal(0,sig,len(samples))
    chanOut = np.convolve(samples,h3,mode = 'full') 
    sampl_n = samples + noise
    noise = np.random.normal(0, sig, len(samples) + len(h3)-1) + 1j * np.random.normal(0,sig,len(samples)+ len(h3)-1)
    sampl_n_ch = chanOut + noise
    mat_h = toeplitz(np.concatenate([h3[1:], np.zeros(3)]),np.concatenate([h3[:2][::-1], np.zeros(3)]))
    d = np.zeros(len(h3)+2)
    d[1] = 1
    inv_mat = np.linalg.inv(mat_h)
    c = helper_func.matrix_vector_multiply(inv_mat,d)   
    equaliz = np.convolve(sampl_n_ch, c, mode = 'full')
    equaliz = equaliz[1+2:]
    equaliz = equaliz[:len(samples)]        
    ser_n = SER(sampl_n,samples)
    ser_ch = SER(equaliz,samples)
    ser_n_mass.append(ser_n)
    ser_ch_mass.append(ser_ch)
    
ser_n_mass = np.asarray(ser_n_mass)
ser_ch_mass = np.asarray(ser_ch_mass)
plt.figure()
plt.title('SER')
# plt.semilogy(snr, ser_n_mass, color='r')
plt.semilogy(snr, ser_n_mass, color='r', label = "AWGN")
plt.semilogy(snr, ser_ch_mass, color='b', label = "Channel + AWGN")
plt.xlabel('SNR (дБ)')
plt.ylabel('error')
    
plt.grid(True)
plt.legend()
        

#ser_channel(samples, snr, h3)
