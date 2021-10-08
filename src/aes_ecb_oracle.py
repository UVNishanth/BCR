# aes_ecb_oracle.py
import sys

import crypto

sys.modules['Crypto'] = crypto
from Crypto.Cipher import AES
import binascii
import time
from Crypto.Random import get_random_bytes

# Set Variables
# -------------------------------
# keey that will be used for encryption (16 bytes)
class Oracle:

    def __init__(self):
        self.key = get_random_bytes(16)
        self.cipher = AES.new(self.key, AES.MODE_ECB)
        self.first = 0
        self.padding = 0
    #print("Key = ", key)
    # tooken or secret information (<= 16 chars)

    def get_token(self):
        return self.token

    def set_target_message(self, target):
        self.token = target

    # Cipher
    # -------------------------------
    # Encrypt a string
    # -------------------------------
    def initiate_encryption(self):
        return self.oracle()

    def encrypt(self, message):
        return self.cipher.encrypt(message)

    def decrypt(self, ciphertext):
        ans = self.cipher.decrypt(ciphertext)
        hex_val = self.byte_to_hex(ans).decode()
        fin = bytearray.fromhex(hex_val).decode()
        prefix_slice = fin[39:]
        return prefix_slice[:-self.padding]


    # Encrypt a message including the string target
    #	display everything oracle knows if display = True
    # -------------------------------
    def oracle(self, target='a' * 27, display = False, see_oracle = False, timing = False):
        message = self.getPadding("data=" + target + ",token=" + self.token)
        message_encoded = message.encode()
        encrypted = self.encrypt(message_encoded)
        if display:
            if timing: time.sleep(.05)
            self.disp(message, target, encrypted, see_oracle)
        encrypted_decoded = self.byte_to_hex(encrypted)
        print("Encrypted decoded", encrypted_decoded)
        return encrypted


    # Padding
    # -------------------------------
    def getPadding(self, secret):
        pl = len(secret)
        mod = pl % 16
        if mod != 0:
            padding = 16 - mod
            secret += 'X' * padding
            if self.first == 0:
                self.padding = padding
                self.first = 1
        return secret

    # For display purposes
    # -------------------------------

    def byte_to_hex(self, elt): return binascii.hexlify(elt)

    def disp(self, message, target, encrypted, see_oracle):
        if see_oracle: print("\nMessage to encrypt: ", message)
        else: print("\nMessage to encrypt: ?")
        print("Target given: ", target)
        if see_oracle:
            print("Message Split", message[0:16], " ", message[16:32], " ", message[32:48], " ", message[48:64], " ", message[64:80], " ", message[80:96], " ")
            print("Secret we don't know:", self.token)
            print("\tEncrypting with AES-ECB.... \n\tkeey =", self.key)
        else: print("Message Split", message[0:16], " ", message[16:32], " ", 16 * "?", " ", 16 * "?", " ", "?" * 16, " ", "?" *16, " ")
        print("Encrypted:", self.byte_to_hex(encrypted), "\n\n")