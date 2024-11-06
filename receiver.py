import functions as func
import numpy as np
import radio_channel as rd

def decoder(code):
    decoded_message = ""
    for i in range(0, len(code), 7):
        chunk = code[i:i + 7]
        decoded_message += chr(int(chunk, 2))
    return decoded_message

def main():
    # Синхронизация с сигналом и отброс лишних нулей в массиве
    signal, length = rd.main()
    golden, G = func.Gold()
    golden = np.repeat(golden, 4)

    autocor = [np.sum(golden * signal[i:i + len(golden)]) for i in range(len(signal) - len(golden))]
    maximum, pos = max(autocor), np.argmax(autocor)
    
    print("Автокорреляция:", maximum)

    synsig = signal[pos: pos + length]
    func.graphic(autocor, "Автокорреляция")
    func.graphic(synsig, "Синхросигнал")

    # Преобразование временных отсчётов в информацию и избавление от шума
    cipher = [1 if synsig[i * 4] > 0.5 else 0 for i in range(len(synsig) // 4)]

    # Удаление последовательности Голда
    ciphernotgold = cipher[G:]

    # Проверка CRC
    CRC = func.CRC(ciphernotgold)
    print("CRC:", CRC)

    if 1 in CRC:
        print("Ошибка CRC")
    else:
        # Удаление CRC и декодирование битов информации в буквы
        word = ciphernotgold[:-7]
        decoded_message = decoder(word)
        clean_message = "".join([i if 65 < ord(i) < 90 else " " + i for i in decoded_message])
        print(clean_message[1:])

if __name__ == "__main__":
    main()
