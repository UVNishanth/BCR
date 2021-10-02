import rsa

def generate_keys():
    return rsa.newkeys(512)

def encrypt(plaintext, pub_key):
    temp = ""
    for p in plaintext:
        temp += str(ord(p))
    temp = int(temp)
    return pow(temp, )

def decrypt(c, priv_key):
    return rsa.decrypt(c, priv_key).decode('utf8')


plaintext = 'hello'
(pub_key, priv_key) = generate_keys()
ciphertext = encrypt(plaintext, pub_key)
print(decrypt(ciphertext, priv_key))
