import numpy as np
import funct as func
import matplotlib.pyplot as plt
import math
%matplotlib
'''
def normalize_autocorrelation(autocor):
    max_value = np.max(autocor)
    min_value = np.min(autocor)
    normalized_autocorrelation = (autocor - min_value) / (max_value - min_value)
    return normalized_autocorrelation, max_value
def normalize_autocorrelation(x, y):
    #x = aut
    #y = golden
    # Вычисляем скалярное произведение векторов x и y
    dot_product = sum(i * j for i, j in zip(x, y))    
    # Вычисляем сумму квадратов элементов векторов x и y
    sum_of_squares_x = sum(i ** 2 for i in x)
    sum_of_squares_y = sum(j ** 2 for j in y)
    # Вычисляем знаменатель корня
    denominator = math.sqrt(sum_of_squares_x * sum_of_squares_y)
    # Проверяем, что знаменатель не равен нулю, чтобы избежать деления на ноль
    if denominator == 0:
        raise ValueError("Ошибка нормализация прошла не успешно")
    # Вычисляем и возвращаем результат выражения
    normalized_autocorrelation = dot_product / denominator
    return normalized_autocorrelation
'''
def add_noise_and_decode(signal, standard_deviation, length):
    
    signal = np.asarray(signal)

    noise = np.random.normal(0, standard_deviation, len(signal))
    signal_with_noise = signal + noise

    func.graphic(signal_with_noise, "Сигнал с шумом")

    gold, G = func.Gold()
    golden = np.repeat(gold, 4)

    autocor = []
    normalized_autocorrelation = []
    sumanormalx = 0
    
    for j in range(len(golden)):
        sumanormalx = sumanormalx + (golden[j] * golden[j])
        
    #autocor = [np.sum(golden * signal_with_noise[i:i + len(golden)]) for i in range(len(signal_with_noise) - len(golden))]
    
    for i in range(len(signal_with_noise) - len(golden)):
        suma = 0
        sumanormaly = 0
        for j in range(len(golden)):
            try:
                suma = suma + (golden[j] * signal_with_noise[i + j])
                sumanormaly = sumanormaly + (signal_with_noise[i + j] * signal_with_noise[i + j])
            except IndexError:
                break
        autocor.append(suma)
        normalized_autocorrelation.append(suma/np.sqrt(sumanormalx*sumanormaly))
    pos = np.argmax(autocor)
    
    """col = 0
    normalized_autocorrelation = []
    while col < (len(autocor)-124):
        seq = autocor[::-1]
        del seq[:933-col]
        aut = seq[::-1]
        del aut[:col]
        normalized_autocorrelation.append(normalize_autocorrelation(aut, gold))
        col += 1
    """

    func.graphic(normalized_autocorrelation, "Автокорреляция")

    synsig = signal_with_noise[pos: pos + length]
    func.graphic(synsig, "Синхросигнал")
    
    cipher = [1 if synsig[i * 4] > 0.5 else 0 for i in range(len(synsig) // 4)]

    ciphernotgold = cipher[G:]

    CRC = func.CRC(ciphernotgold)
    print("CRC:", CRC)

    if 1 in CRC:
        print("Ошибка CRC")
    else:
        word = []
        for i in range(len(ciphernotgold) - 7):
            word.append(ciphernotgold[i])
        donemas = func.decoder(word)
        done = ""
        for i in donemas:
            if ord(i) > 65 and ord(i) < 90:
                done += " "
            done += i
        print(done[1:])

def generate_signal_and_transmit(name):

    kod = func.coder(name)
    func.graphic(kod, "Кодирование символов")
    
    M = len(kod)
    delet = [1, 1, 1, 1, 1, 0, 1, 1]
    
    for i in range(len(delet) - 1):
        kod.append(0)
    
    CRCnum = func.CRC(kod)
    print("CRC:", CRCnum)

    for i in range(M, len(kod)):
        kod[i] = CRCnum[i - M]


    golden, G = func.Gold()
    
    for i in range(G):
        kod.append(0)
        kod = func.shiftright(kod)  
    
    for i in range(G):
        kod[i] = golden[i]
    
    func.graphic(kod, "Кодирование с голдом и CRC и Голдом")
    
    otch = 4
    signal = np.repeat(kod, otch)
    func.graphic(signal, "Отсчёты")
    length = len(signal)

    bigsignal = [int(0) for i in range(2 * len(signal))]
    key = int(input("Введите число для вставки в массив: "))
    
    while 1 == 1:
        if key > 0 and key < len(signal):
            break
        else:
            print("Недопустимое число, введите ещё раз")
            key = int(input())
    
    for i in range(len(bigsignal)):
        if i >= key and i - key < len(signal):
            bigsignal[i] = signal[i - key]
        else:
            bigsignal[i] = 0
            
    func.graphic(bigsignal, "Сигнал с передатчика")
    
    return bigsignal, length

def main():
    
    name = input("Введите имя и фамилию: ")
    signal, length = generate_signal_and_transmit(name)
    add_noise_and_decode(signal, 0.15, length)

if __name__ == "__main__":
    main()


