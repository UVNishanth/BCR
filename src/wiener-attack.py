import binascii
import time

import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator
import rsa
from Caesar import Caesar

class RSA:

    def __init__(self):
        pass
    def generate_keys(self):
        self.e, self.n, self.d, self.p, self.q = RSAvulnerableKeyGenerator.generateKeys(512)
        self.pub_key = rsa.PublicKey(self.n, self.e)

    def encrypt(self, message):
        #enc = message
        return rsa.encrypt(message, self.pub_key)

    def decrypt(self, ciphertext, priv_key):
        return rsa.decrypt(ciphertext, priv_key)

    def get_private_key(self, d):
        return rsa.PrivateKey(self.n, self.e, d, self.p, self.q)

    def get_actual_d(self):
        return self.d


    def hack_RSA(self):
        '''
        Finds d knowing (e,n)
        applying the Wiener continued fraction attack
        '''
        e = self.e
        n = self.n
        frac = ContinuedFractions.rational_to_contfrac(e, n)
        convergents = ContinuedFractions.convergents_from_contfrac(frac)

        for (k, d) in convergents:

            #check if d is actually the key
            if k!=0 and (e*d-1)%k == 0:
                phi = (e*d-1)//k
                s = n - phi + 1
                # check if the equation x^2 - s*x + n = 0
                # has integer roots
                discr = s*s - 4*n
                if(discr>=0):
                    t = Arithmetic.is_perfect_square(discr)
                    if t!=-1 and (s+t)%2==0:
                        print("Hacked!")
                        return d




plaintext = b'abceffg'

#plaintext = "12345".encode('utf-8')
rsa_mod = RSA()
rsa_mod.generate_keys()
priv_key = rsa_mod.get_private_key(rsa_mod.get_actual_d())
c_text = rsa_mod.encrypt(plaintext)
print(type(c_text))

c_text_hex = c_text.hex()
print("ciphertext: ", c_text)
print("ciphertext after hex: ", c_text_hex)

#p_text = rsa_mod.decrypt(c_text, priv_key)"""
hacked_d = rsa_mod.hack_RSA()
hacked_priv_key = rsa_mod.get_private_key(hacked_d)
hacked_ptext = rsa_mod.decrypt(c_text, hacked_priv_key)

print("Actual plaintext: ", plaintext, " derived plaintext is: ", hacked_ptext)

caesar = Caesar()
c_text_caesar = caesar.encryptCaesar(c_text_hex, 2203)
print("cipher after caesar: ", c_text_caesar)

caesar_p = caesar.decryptCaesar(c_text_caesar, 2203)
possible = caesar.frequencyAttack(c_text_caesar)
print("decrypted_Caesar: ", caesar_p)
print("possible: ", possible)
x = bytes.fromhex(caesar_p)
rsa_p = rsa_mod.decrypt(x, priv_key)
print("rsa_p", rsa_p)
#print("possible: ", possible)


# print("plain after caesar: ", caesar_p)

"""for element in possible:
    try:
        x = bytes.fromhex(element)
        rsa_p = rsa_mod.decrypt(x, priv_key)
        print("rsa_p", rsa_p)
    except(Exception):
        print("Not a hex")"""


