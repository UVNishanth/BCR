import binascii
import time

import crypto
import sys
sys.modules['Crypto'] = crypto
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from aes_ecb_attack import Attack
from aes_ecb_oracle import Oracle

oracle = Oracle()
target_message = input("Target Message: ")
oracle.set_target_message(target_message)
ciphertext = oracle.initiate_encryption()
p = oracle.decrypt(ciphertext)

attack = Attack(oracle)
plaintext = attack.start_attack_and_get_plaintext()
print("p type: ", type(p))
print("Ciphertext: ", oracle.byte_to_hex(ciphertext), " \nplaintext: ", plaintext)
print("Decryption via decrypt: ", p)



# key = get_random_bytes(16)
# print("Key = ", key)
# # tooken or secret information (<= 16 chars)
#
# # Cipher
# # -------------------------------
# #cipher = AES.new(start.key, AES.MODE_ECB)
#
# def byte_to_hex(elt): return binascii.hexlify(elt)
#
# cipher = AES.new(key, AES.MODE_ECB)
# encryption = cipher.encrypt(("data=aaaaaaaaaaaaaaaaaaaaaaaaaaa,tooken="+token).encode())
# print("What we get from encrption: ", (byte_to_hex(encryption)))
# time.sleep(10)
#
# #c = cipher.encrypt("aaaaaaaaaaaaaaaaaaaaaaaanishanth".encode())
# #print("Ciphertext: ", c)
#
# start(encryption, key)



