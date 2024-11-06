import numpy as np

name = input("Enter your name: ")
surname = input("Enter your surname: ")

def ascii_to_binary(text):
    return ''.join(format(ord(i), '08b') for i in text)

binary_name = ascii_to_binary(name)
binary_surname = ascii_to_binary(surname)

binary_sequence = binary_name + binary_surname

def crc(data, generator, crc_length):
    data = list(data) + [0]*crc_length
    while '1' in data[:-crc_length]:
        cur_shift = data.index('1')
        for i in range(len(generator)):
            data[cur_shift+i] = str(int(generator[i]!=data[cur_shift+i]))
    return ''.join(map(str, data[-crc_length:]))

generator = '1011'
crc_length = 4
crc_code = crc(binary_sequence, generator, crc_length)

def gold_sequence(length):
    seq = [0]*length
    for i in range(2, length):
        seq[i] = (seq[i-1] + seq[i-2]) % 2
    return seq

gold_length = len(binary_sequence)
gold_code = gold_sequence(gold_length)

def bit_to_signal(bit, signal_length):
    return [str(bit)]*signal_length

signal_length = 4
signal_sequence = [bit_to_signal(bit, signal_length) for bit in ''.join(binary_sequence+crc_code+gold_code)]