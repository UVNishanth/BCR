import time

import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator
import rsa

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)

    for (k,d) in convergents:

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

print("Testing Wiener Attack")
times = 1

e,n,d,p,q = RSAvulnerableKeyGenerator.generateKeys(1024)
#print("(e,n) is (", e, ", ", n, ")")
#print("d = ", d)

start = time.time()
hacked_d = hack_RSA(e, n)
end = time.time()
print("Time taken to hack: ", (end-start))


plaintext = "abcdefgh".encode('utf-8')

if d == hacked_d:
    print("Hack WORKED!")
    print("The actual private key is: ", d, " and the hacked private key is: ", hacked_d)
    pub_key = rsa.PublicKey(n, e)
    priv_key = rsa.PrivateKey(n, e, hacked_d, p, q)
    cipher = rsa.encrypt(plaintext, pub_key)
    print("ciphertext is: "+str(cipher))
    p = rsa.decrypt(cipher, priv_key)
    print("hecked plaintext is: "+p.decode('utf-8'))
else:
    print("Hack FAILED")