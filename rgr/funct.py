import numpy as np
import matplotlib.pyplot as plt

def decoder(code):
    sim = ""
    decode = []
    j = 0
    for i in code:
        if j == 7:
            decode.append(chr(int(sim, 2)))
            j = 0
            sim = ""
        sim += str(i)
        j += 1
    decode.append(chr(int(sim, 2)))
    return decode

def coder(text):
    mas = [ord(i) for i in text if i != " "]
    code = [int(bit) for char in mas for bit in bin(char)[2:]]
    return code

def add_noise(signal, standard_deviation):
    signal = np.asarray(signal)
    noise = np.random.normal(0, standard_deviation, len(signal))
    return signal + noise

def graphic(mas, title):

    buk = np.asarray(mas)
    plt.figure()
    plt.title(title)
    plt.plot(buk)

def CRC(pack):
    delet = [1, 1, 1, 1, 1, 0, 1, 1]
    ost = [i for i in range(len(delet))]

    for i in range(len(delet) - 1):
        ost[i] = pack[i + 1] ^ delet[i + 1]

    ost[len(delet) - 1] = pack[len(delet)]

    for i in range(len(delet) + 1, len(pack)):
        if ost[0] != 0:
            for j in range(len(delet) - 1):
                ost[j] = ost[j + 1] ^ delet[j + 1]
        else:
            for j in range(len(delet) - 1):
                ost[j] = ost[j + 1]
        ost[len(delet) - 1] = pack[i]
    
    if ost[0] != 0:
        for j in range(len(delet)):
            ost[j] = ost[j] ^ delet[j]
    
    return ost[1:]

def shiftright(mas):
    temp = mas[len(mas) - 1]
    for i in range(len(mas) - 1, 0, -1):
        mas[i] = mas[i - 1]
    mas[0] = temp
    return mas

def Gold():
    x = [0, 0, 1, 0, 0]
    y = [0, 1, 0, 1, 1]
    G = 31
    itog = []
    
    for i in range(G):
        summatorx = x[2] ^ x[3]
        summatory = y[2] ^ y[1]
        itog.append(x[4] ^ y[4])
        x = shiftright(x)
        y = shiftright(y)
        x[0] = summatorx
        y[0] = summatory
    
    return itog, G

"""def receive_and_process():
    signal, length = base.main()
    standard_deviation = float(input("Введите стандартное отклонение: "))
    
    signal_with_noise = add_noise(signal, standard_deviation)
    
    graphic(signal_with_noise, "Сигнал с шумом")

    delet_sequence, G = Gold()

    autocorrelation = []
    for i in range(len(signal_with_noise) - len(delet_sequence)):
        summation = np.sum(delet_sequence * signal_with_noise[i:i + len(delet_sequence)])
        autocorrelation.append(summation)
    
    maximum, pos = max(autocorrelation), np.argmax(autocorrelation)

    print("Автокорреляция:", maximum)

    synchronized_signal = signal_with_noise[pos: pos + length]
    graphic(autocorrelation, "Автокорреляция")
    graphic(synchronized_signal, "Синхросигнал")

    cipher = [1 if synchronized_signal[i * 4] > 0.5 else 0 for i in range(len(synchronized_signal) // 4)]

    ciphernotgold = cipher[G:]

    CRC_result = CRC(ciphernotgold)
    print("CRC:", CRC_result)

    if 1 in CRC_result:
        print("Ошибка CRC")
    else:
        word = ciphernotgold[:-7]
        decoded_message = decoder(word)
        clean_message = "".join([i if 65 < ord(i) < 90 else " " + i for i in decoded_message])
        print(clean_message[1:])"""

if __name__ == "__main__":
    receive_and_process()
