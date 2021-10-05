import math

import rsa

def generate_keys():
    return rsa.newkeys(512)

def encrypt(plaintext, N, e):
    #p = plaintext.encode('utf8')
    temp = ""
    """for c in plaintext:
        temp += str(ord(c))
    print(temp)
    temp =int(temp)"""
    return math.pow(plaintext, e)%N
    #return rsa.encrypt(p, pub_key)

def decrypt(c, priv_key):
    return rsa.decrypt(c, priv_key).decode('utf8')


plaintext = 'hello'
#(pub_key, priv_key) = generate_keys()

#ciphertext = encrypt(plaintext, N,)
#print(decrypt(ciphertext, priv_key))
