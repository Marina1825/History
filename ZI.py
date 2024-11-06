from math import sqrt
#----------------------------------Задача 1---------------------------------#
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
# Вводные данны: base^exp % mod
base =  15
exp = 18
mod = 10
result = fast_exp_mod_recursive(base, exp, mod)
print(f"#-----------------------------------------------------------------#")
print(f"1) {base}^{exp} mod {mod} = {result}")
#----------------------------------Задача 2---------------------------------#
def extended_gcd(a, b):
    if a < 0 or b < 0:
        raise ValueError("Числа должны быть положительными")
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


# Пример использования
a = 64
b = 47
gcd, x, y = extended_gcd(a, b)
print(f"#-----------------------------------------------------------------#")
print(f"2) {a}x + {b}y = НОД({a}, {b}) = {gcd}")
print(f"Коэффициенты x и y: x = {x}, y = {y}")
print(f"{a} * {x} + {b} * {y} = {gcd}")
#----------------------------------Задача 3--------------------------------#
def diffie_hellman(p, g, private_key_a, private_key_b):
    if p <= 1 or g <= 1:
        raise ValueError("p и g должны быть больше 1")
    if g >= p:
        raise ValueError("g должно быть меньше p")
    # Вычисление открытых ключей для каждого абонента
    public_key_a = fast_exp_mod_recursive(g, private_key_a, p)
    public_key_b = fast_exp_mod_recursive(g, private_key_b, p)
    
    # Вычисление общего секретного ключа для каждого абонента
    shared_secret_a = fast_exp_mod_recursive(public_key_b, private_key_a, p)
    shared_secret_b = fast_exp_mod_recursive(public_key_a, private_key_b, p)
    
    # Проверка, что оба абонента получили одинаковый секретный ключ
    assert shared_secret_a == shared_secret_b
    
    return shared_secret_a

# Пример использования
p = 23  # Простое число
g = 5   # Примитивный корень по модулю p

private_key_a = 6  # Секретный ключ абонента A
private_key_b = 15  # Секретный ключ абонента B

shared_secret = diffie_hellman(p, g, private_key_a, private_key_b)
print(f"#-----------------------------------------------------------------#")
print(f"3) Общий секретный ключ: {shared_secret}")
#----------------------------------Задача 4--------------------------------#
def baby_step_giant_step(g, h, p):
    if p <= 1 or g <= 1 or h <= 1:
        raise ValueError("p, g и h должны быть больше 1")
    if g >= p or h >= p:
        raise ValueError("g и h должны быть меньше p")

    n = int(sqrt(p)) + 1
    baby_steps = {}

    for j in range(n):
        baby_steps[fast_exp_mod_recursive(g, j, p)] = j

    g_inv = pow(g, -n, p)
    for i in range(n):
        y = (h * fast_exp_mod_recursive(g_inv, i, p)) % p
        if y in baby_steps:
            return i * n + baby_steps[y]

    return None

# Пример использования
g = 5
h = 3
p = 23

result = baby_step_giant_step(g, h, p)
print(f"#-----------------------------------------------------------------#")
if result is not None:
    print(f"4) Решение x: {result}")
else:
    print("4) Решение не найдено")