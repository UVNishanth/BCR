import random

def check_validity(k):
    a_shift = int(k / 100)
    n_shift = k % 100
    if a_shift % 26 != 0 and n_shift !=0 and n_shift <= 9:
        return True
    return False

def generate_random_key():
    while True:
        k = random.randint(1000, 9999)
        if check_validity(k):
            break
    return k

def encrypt(plaintext, key):
    a_key = int(key / 100)
    n_key = key % 100
    result = ''
    for c in plaintext:
        if c.isnumeric():
            new_c = int(c) - n_key
            if(new_c <0):
                new_c = int(9 + new_c + 1)
            result += str(new_c)
        else:
            new_c = ord(c) + a_key
            if new_c >= ord('a'):
                z_greater = new_c > ord('z')
                z_less = new_c <= ord('z')
                result += chr(((new_c) % ((ord('z') * z_greater + (ord('a') * z_less)))) + (
                            (ord('a') - 1) * z_greater + (ord('a') * z_less)))
            else:
                result += chr(new_c + 26)
    return result

def decrypt(ciphertext, key):
    a_key = int(key / 100)
    n_key = key % 100
    result = ''
    for c in ciphertext:
        if c.isnumeric():
            new_c = int(c) + n_key
            if(new_c >= 10):
                new_c = int(new_c - 9 - 1)
            result += str(new_c)
        else:
            new_c = ord(c) - a_key
            if new_c >= ord('a'):
                z_greater = new_c > ord('z')
                z_less = new_c <= ord('z')
                result += chr(((new_c) % ((ord('z') * z_greater + (ord('a') * z_less)))) + (
                            (ord('a') - 1) * z_greater + (ord('a') * z_less)))
            else:
                result += chr(new_c + 26)
    return result

print(encrypt("z24", 1007))

print(decrypt("j57", 1007))


#print(generate_random_key())