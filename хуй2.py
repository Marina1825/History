import numpy as np
import random
import matplotlib.pyplot as plt

bool_print = 0 
lable_grey = 0
ser_plot   = 0

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return np.asarray(list(map(int,bits.zfill(8 * ((len(bits) + 7) // 8)))))

def bits_array_to_text(bits_array):
    bits_string = ''.join([str(bit) for bit in bits_array])
    bits_string = bits_string.replace(" ", "")
    n = int(bits_string, 2)
    text = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('latin1')
    return text

def bits_to_number(bits):
    if len(bits) % 4 != 0:
        raise ValueError("Длина массива должна быть кратна 4.")
    # Разбиваем массив битов на блоки по 4
    blocks = [bits[i:i+4] for i in range(0, len(bits), 4)]
    # Преобразуем каждый блок в число
    result = [int("".join(map(str, block)), 2) for block in blocks]
    return result

def split_array(input_array, chunk_size=4):
    return [str(input_array[i:i + chunk_size]) for i in range(0, len(input_array), chunk_size)]

def QAM16(bit_mass):
	if (len(bit_mass) % 4 != 0):
		print("QAM16:\nError, check bit_mass length")
		raise "error"
	else:
		sample = []
		for i in range(0, len(bit_mass), 4):
			b4i = bit_mass[i]
			b4i1 = bit_mass[i+1]
			b4i2 = bit_mass[i+2]
			b4i3 = bit_mass[i+3]
			real = (1 - 2 * b4i) * (2 - (1 - 2 * b4i2))
			imag = (1 - 2 * b4i1) * (2 - (1 - 2 * b4i3))
			sample.append(complex(real, imag))
		sample = np.asarray(sample)
		return sample

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

def randomDataGenerator(size):
	data = [random.randint(0, 1) for i in range(size)]
	return data

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

def probability(sample, sig, pos_bit, bit):
    #            b0 0      1       b1  0   1
    #orig_sampl = [[-3, -1, 3, 1], [-3, 3, -1, 1]]
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

def qam16_demodulator(signal):
    constellation = np.array([[-3, -3], [-3, -1], [-3, 1], [-3, 3],
                              [-1, -3], [-1, -1], [-1, 1], [-1, 3],
                              [ 1, -3], [ 1, -1], [ 1, 1], [ 1, 3],
                              [ 3, -3], [ 3, -1], [ 3, 1], [ 3, 3]])
    demodulated_bits = []
    for sym in signal:
        distances = np.sqrt((constellation[:, 0] - np.real(sym))**2 + (constellation[:, 1] - np.imag(sym))**2)
        closest_point = constellation[np.argmin(distances)]
        bits = []
        for val in closest_point:
            if val == -3:
                bits.extend([0, 0])
            elif val == -1:
                bits.extend([0, 1])
            elif val == 1:
                bits.extend([1, 1])
            elif val == 3:
                bits.extend([1, 0])
        demodulated_bits.extend(bits)
    return demodulated_bits

text = ''

mass_bit = randomDataGenerator(100000)
qam_16 = [-3, 3, -1, 1]
mass_code_grey = code_Grey_16(mass_bit)

samples = mapping(mass_code_grey)

if 0:
    plt.figure()
    plt.scatter(samples.real, samples.imag )

lable_bit = split_array(mass_code_grey)

if lable_grey:
    for i in range(len(samples)):
        plt.text(samples[i].real, samples[i].imag, lable_bit[i])  

ser_mass = []
snr = np.arange(0,30,1)

def sigma(snr,samples):
    h2 = 10**(0.1*snr)
    Ps = np.sum(abs(samples)**2)/len(samples)
    sigma = np.sqrt(Ps/h2)
    return sigma

if ser_plot:
    for i in range(len(snr)):
        sig = sigma(snr[i],samples)        
        noise = np.random.normal(0, sig, len(samples)) + 1j * np.random.normal(0,sig,len(samples))
        sampl_n = samples + noise
        ser = SER(sampl_n,samples)
        ser_mass.append(ser)

#error_symbol(qam_16, samples)
if ser_plot:
    plt.figure()
    plt.semilogy(snr, ser_mass, color='r')
    plt.xlabel('SNR (дБ)')
    plt.ylabel('error')
    plt.title('SER')
    plt.grid(True)
    plt.figure()
    print(ser)
    plt.scatter(sampl_n.real, sampl_n.imag )
    plt.scatter(samples.real, samples.imag )

sig = sigma(23, samples)
noise = np.random.normal(0, sig, len(samples)) + 1j * np.random.normal(0,sig,len(samples))

# print(mass_bit)
# print(mass_code_grey)
sampl_n = samples + noise

if 0:
    plt.figure()
    plt.scatter(sampl_n.real, sampl_n.imag )

dec = qam16_demodulator(sampl_n)

error_bit_soft = []
error_bit_hard = []
if 1:
    for i in range(len(snr)):
        sig = sigma(snr[i],samples)
        noise = np.random.normal(0, sig, len(samples)) + 1j * np.random.normal(0,sig,len(samples))
        sampl_n = samples + noise
        decode = likelihood_ratio(sampl_n,sig)
        err = np.sum(decode != mass_code_grey)
        ratio_err = err / len(decode)
        error_bit_soft.append(ratio_err)

if 1:
    plt.figure()
    plt.semilogy(snr, error_bit_soft, color='r', label = "Softbit")
    plt.xlabel('SNR (дБ)')
    plt.ylabel('error')
    plt.title('BER QAM16')
    plt.grid(True)

if 1:
    for i in range(len(snr)):
        sig = sigma(snr[i],samples)
        noise = np.random.normal(0, sig, len(samples)) + 1j * np.random.normal(0,sig,len(samples))
        sampl_n = samples + noise
        decode = qam16_demodulator(sampl_n)
        err = np.sum(decode != mass_code_grey)
        ratio_err = err / len(decode)
        error_bit_hard.append(ratio_err)
if 1:
    plt.semilogy(snr, error_bit_hard, color='b', label = "Hardbit")
    plt.xlabel('SNR (дБ)')
    plt.ylabel('error')
    # plt.title('BER HARD')
    plt.grid(True)

plt.legend()
plt.show()