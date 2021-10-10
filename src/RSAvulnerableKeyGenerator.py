'''

Referred to https://github.com/pablocelayes/rsa-wiener-attack

'''

import random, MillerRabin, Math_utils

def getPrimePair(bits=512):


    assert bits%4==0

    p = MillerRabin.gen_prime(bits)
    q = MillerRabin.gen_prime_range(p + 1, 2 * p)

    return p,q

def generateKeys(nbits=1024):
    # nbits >= 1024 is recommended
    assert nbits%4==0

    p,q = getPrimePair(nbits//2)
    n = p*q
    phi = Math_utils.totient(p, q)

    # generate a d such that:
    #     (d,n) = 1
    #    36d^4 < n
    good_d = False
    while not good_d:
        d = random.getrandbits(nbits//4)
        if (Math_utils.gcd(d, phi) == 1 and 36*pow(d, 4) < n):
            good_d = True

    e = Math_utils.modInverse(d, phi)
    return e,n,d,p,q
