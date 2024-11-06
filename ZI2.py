import getpass

def fast_exp_mod_recursive(base, exp, mod):
    if mod <= 0:
        raise ValueError("Модуль не должен быть меньше нуля")
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        half_exp = fast_exp_mod_recursive(base, exp // 2, mod)
        return (half_exp * half_exp) % mod
    else:
        return (base * fast_exp_mod_recursive(base, exp - 1, mod)) % mod

def Shamir():
    #Шифр Шамиля
    print("Шифр Шамиля")
    # Запрос секретного сообщения
    m = int(input("Введите секретное сообщения: "))
    p = int(input("ВВедите число p: "))

    Ca = int(input("Абонент А, введите число Са: "))
    Da = int(input("Введите число Da: "))
    Cb = int(input("Абонент B, введите число Сb: "))
    Db = int(input("Введите число Db: "))

    x1 = fast_exp_mod_recursive(m, Ca, p)
    x2 = fast_exp_mod_recursive(x1, Cb, p)
    x3 = fast_exp_mod_recursive(x2, Da, p)
    x4 = fast_exp_mod_recursive(x3, Db, p)

    print(f"Секретное число: {x4}")
    return x4

def ElGamal():
    print("Шифр Эль-Гамаля")
    p = 23
    g = 5
    #12 13
    Ca = int(getpass.getpass("Абонент А, введите секретный ключ: "))
    Cb = int(getpass.getpass("Абонент B, введите секретный ключ: "))
    
    # Открытые ключи
    Da = fast_exp_mod_recursive(g, Ca, p)
    Db = fast_exp_mod_recursive(g, Cb, p)
    #15 7
    m = int(getpass.getpass("Абонент А, введите секретное сообщения: "))
    k = int(input("Введите случайное число k: "))
            
    r = fast_exp_mod_recursive(g, k, p)
    e = fast_exp_mod_recursive(m*Db, k, p)
    
    m1 = fast_exp_mod_recursive(e*r, p-1-Cb, p)
    
    print(f"Секретное число: {m1}")
    return m1

# Шифр Вернама
def vernam_encrypt(message, key):
    # Преобразование сообщения и ключа в битовый формат
    message_bits = ''.join(format(ord(c), '08b') for c in message)
    key_bits = ''.join(format(ord(c), '08b') for c in key)
    
    # Шифрование сообщения
    encrypted_bits = ''.join('1' if message_bits[i] != key_bits[i] else '0' for i in range(len(message_bits)))
    
    # Преобразование битов в символы
    encrypted_message = ''.join(chr(int(encrypted_bits[i:i+8], 2)) for i in range(0, len(encrypted_bits), 8))
    
    return encrypted_message

def vernam_decrypt(encrypted_message, key):
    # Преобразование зашифрованного сообщения и ключа в битовый формат
    encrypted_bits = ''.join(format(ord(c), '08b') for c in encrypted_message)
    key_bits = ''.join(format(ord(c), '08b') for c in key)
    
    # Дешифрование сообщения
    decrypted_bits = ''.join('1' if encrypted_bits[i] != key_bits[i] else '0' for i in range(len(encrypted_bits)))
    
    # Преобразование битов в символы
    decrypted_message = ''.join(chr(int(decrypted_bits[i:i+8], 2)) for i in range(0, len(decrypted_bits), 8))
    
    return decrypted_message

if __name__ == "__main__":
    
    otvet = Shamir()
    otvet = ElGamal()

        
    message = "7418"
    key = "ZCXC"
    encrypted_message = vernam_encrypt(message, key)
    decrypted_message = vernam_decrypt(encrypted_message, key)
    print(f"Vernam: {encrypted_message}")
    print(f"Vernam: {decrypted_message}")