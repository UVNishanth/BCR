import time

import ContinuedFractions, Math_utils, RSAvulnerableKeyGenerator
import rsa


class RSA:

    def __init__(self):
        pass
    def generate_keys(self):
        self.e, self.n, self.d, self.p, self.q = RSAvulnerableKeyGenerator.generateKeys(512)
        self.pub_key = rsa.PublicKey(self.n, self.e)
        #print("Public key is: ", self.pub_key)

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
                    t = Math_utils.is_perfect_square(discr)
                    if t!=-1 and (s+t)%2==0:
                        print("Hacked!")
                        return d
