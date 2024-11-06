import random
from math import gcd

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    def miller_rabin_test(d, n):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        if not miller_rabin_test(d, n):
            return False
    return True

def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

def mod_inverse(e, phi):
    """Вычисление мультипликативной инверсии с использованием расширенного алгоритма Евклида."""
    return pow(e, -1, phi)

def generate_keypair(bits):
    """Генерация пары ключей (открытый и закрытый)."""
    p = 7
    q = 17
    n = p * q
    phi = (p - 1) * (q - 1)

    # Выбираем открытую экспоненту e
    e = 5
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Вычисляем секретную экспоненту d
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)

if __name__ == "__main__":
    # Генерация ключей
    public_key, private_key = generate_keypair(1024)
    print(f"Открытый ключ: {public_key}")
    print(f"Закрытый ключ: {private_key}")

    # Шифрование и дешифрование сообщения
    message = "Hello, RSA!"
    print(f"Исходное сообщение: {message}")

    encrypted_message = encrypt(public_key, message)
    print(f"Зашифрованное сообщение: {encrypted_message}")

    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Расшифрованное сообщение: {decrypted_message}")