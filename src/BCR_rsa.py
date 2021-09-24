import rsa

def generate_keys():
    return rsa.newkeys(512)

def encrypt(plaintext, pub_key):
    p = plaintext.encode('utf8')
    return rsa.encrypt(p, pub_key)

def decrypt(c, priv_key):
    return rsa.decrypt(c, priv_key).decode('utf8')


plaintext = 'hello'
(pub_key, priv_key) = generate_keys()
ciphertext = encrypt(plaintext, pub_key)
print(decrypt(ciphertext, priv_key))
