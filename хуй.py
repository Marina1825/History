import matplotlib.pyplot as plt
import random
import numpy as np

def binary_to_qam16(binary):
    amplitude_map = {'00': -3, '01': -1, '10': 1, '11': 3}
    real_part = amplitude_map[binary[0:2]]
    imag_part = amplitude_map[binary[2:4]]
    return complex(real_part, imag_part)

def randomDataGenerator(size):
	data = [random.randint(0, 1) for i in range(size)]
	return data

def sigma(snr,samples):
    h2 = 10**snr
    Ps = np.sum(abs(array_qam16_numbers)**2)/len(array_qam16_numbers)
    sigma = np.sqrt(Ps/h2)
    return sigma

def likelihood_ratio(samples,sig):
    bits_4 = []
    for i in range(len(samples)):
        for pos_bit in range(4):
            P_0 = 0
            P_1 = 0
            ratio = 0
            if pos_bit == 0 or pos_bit == 1:
                P_0 = probability(samples[i].real, sig, pos_bit, 0)
                P_1 = probability(samples[i].real, sig, pos_bit, 1)
                ratio = P_1 / P_0
            if pos_bit == 2 or pos_bit == 3:
                P_0 = probability(samples[i].imag, sig, pos_bit, 0)
                P_1 = probability(samples[i].imag, sig, pos_bit, 1)
                ratio = P_1 / P_0
            if ratio >=1 : 
                bits_4.append(1)
            else:
                bits_4.append(0)
    return bits_4

def probability(sample, sig, pos_bit, bit):
    _one = 0
    _two = 0
    const = 1/(np.sqrt(2*np.pi*sig**2))
    if pos_bit == 0 or pos_bit == 2:
        if bit == 0:
            _one = -3
            _two = -1
        else:
            _one = 3
            _two = 1
    elif pos_bit == 1 or pos_bit == 3:
        if bit == 0:
            _one = -3
            _two =  3
        else:
            _one = -1
            _two =  1
    return const * 2.71828182845904**(-((sample - (_one))**2)/(2*sig**2)) + const * 2.71828182845904**(-((sample - (_two))**2)/(2*sig**2))

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

q = 1

random_bits = [random.randint(0, 1) for i in range(1000)]
random_Grey_bits = code_Grey_16(random_bits)
random_Grey_bits = [str(num) for num in random_Grey_bits]
random_Grey_bits = [''.join(random_Grey_bits[i:i+4]) for i in range(0, len(random_Grey_bits), 4)]
qam16_numbers = [binary_to_qam16(binary) for binary in random_Grey_bits]
array_qam16_numbers = np.array(qam16_numbers)
ideal_points = [binary_to_qam16(bin(i)[2:].zfill(4)) for i in range(16)]
plt.scatter([c.real for c in ideal_points], [c.imag for c in ideal_points], s=100, c='red', marker='x')
plt.scatter([c.real for c in qam16_numbers], [c.imag for c in qam16_numbers], s=50, c='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()
snr = np.arange(0,50,1)
sig = sigma(20, array_qam16_numbers)
noise = np.random.normal(0, sig, len(qam16_numbers)) + 1j * np.random.normal(0,sig,len(qam16_numbers))
def qam16_to_binary(qam16):
    amplitude_map = {(-3, -3): '0000', (-3, -1): '0001', (-3, 1): '0010', (-3, 3): '0011',
                     (-1, -3): '0100', (-1, -1): '0101', (-1, 1): '0110', (-1, 3): '0111',
                     (1, -3): '1000', (1, -1): '1001', (1, 1): '1010', (1, 3): '1011',
                     (3, -3): '1100', (3, -1): '1101', (3, 1): '1110', (3, 3): '1111'}
    
    real_part = np.array(qam16.real)
    imag_part = np.array(qam16.imag)
    
    real_part = np.where(real_part <= -2, -3, real_part)
    real_part = np.where((-2 < real_part) & (real_part < 0), -1, real_part)
    real_part = np.where((0 <= real_part) & (real_part < 2), 1, real_part)
    real_part = np.where(2 <= real_part, 3, real_part)
    
    imag_part = np.where(imag_part <= -2, -3, imag_part)
    imag_part = np.where((-2 < imag_part) & (imag_part < 0), -1, imag_part)
    imag_part = np.where((0 <= imag_part) & (imag_part < 2), 1, imag_part)
    imag_part = np.where(2 <= imag_part, 3, imag_part)
    
    binary_output = []
    for r, i in zip(real_part, imag_part):
        binary_output.append(amplitude_map[(r, i)])
    
    return ''.join(binary_output)

error_bit = []
for i in range(len(snr)):
    noise = np.random.normal(0, sig, len(array_qam16_numbers)) + 1j * np.random.normal(0,sig,len(array_qam16_numbers))
    noisy_qam16_numbers = array_qam16_numbers + noise
    decode = qam16_to_binary(noisy_qam16_numbers)
    err = np.sum(decode != random_Grey_bits)
    ratio_er = err / len(decode)
    error_bit.append(ratio_er)
    
plt.figure()
plt.semilogy(snr, error_bit, color='r', label = "Softbit")
plt.xlabel('SNR (дБ)')
plt.ylabel('error')
plt.title('SER QAM16')
plt.grid(True)

# Шаг 5: Нарисовать созвездие
plt.figure(figsize=(6, 6))
ideal_points = [binary_to_qam16(bin(i)[2:].zfill(4)) for i in range(16)]
plt.scatter([c.real for c in ideal_points], [c.imag for c in ideal_points], s=100, c='red', marker='x')
plt.scatter([c.real for c in noisy_qam16_numbers], [c.imag for c in noisy_qam16_numbers], s=50, c='blue')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.xlabel('Real')
plt.ylabel('Imaginary')
#plt.title('Constellation Diagram for QAM-16 with AWGN (SNR = {} dB)'.format(snr))
plt.show()

error_bit_soft = []
error_bit_hard = []

for i in range(len(snr)):
    sig = sigma(snr[i],qam16_numbers)
    noise = np.random.normal(0, sig, len(array_qam16_numbers)) + 1j * np.random.normal(0,sig,len(array_qam16_numbers))
    noisy_qam16_numbers = array_qam16_numbers + noise
    decode = likelihood_ratio(noisy_qam16_numbers,sig)    
    err = np.sum(decode != random_Grey_bits)
    ratio_err = err / len(decode)
    error_bit_soft.append(ratio_err)

plt.figure()
plt.semilogy(snr, error_bit_soft, color='r', label = "Softbit")
plt.xlabel('SNR (дБ)')
plt.ylabel('error')
plt.title('BER QAM16')
plt.grid(True)

for i in range(len(snr)):
    sig = sigma(snr[i],qam16_numbers)
    noise = np.random.normal(0, sig, len(array_qam16_numbers)) + 1j * np.random.normal(0,sig,len(array_qam16_numbers))
    noisy_qam16_numbers = array_qam16_numbers + noise
    decode = qam16_to_binary(noisy_qam16_numbers)
    err = np.sum(decode != random_Grey_bits)
    ratio_err = err / len(decode)
    error_bit_hard.append(ratio_err)

plt.semilogy(snr, error_bit_hard, color='b', label = "Hardbit")
plt.xlabel('SNR (дБ)')
plt.ylabel('error')
plt.title('BER HARD')
plt.grid(True)

plt.legend()
plt.show()