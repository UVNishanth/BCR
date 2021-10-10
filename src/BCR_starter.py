import time

from BCR_rsa import RSA
from Caesar_Attack import Caesar
from aes_ecb_oracle import Oracle
from aes_ecb_attack import Attack


def test_A(plaintext):
    # Encryption
    #RSA
    orig_plaintext = plaintext
    print("plaintext is: ", orig_plaintext)
    rsa_mod = RSA()
    rsa_mod.generate_keys()
    priv_key = rsa_mod.get_private_key(rsa_mod.get_actual_d())
    plaintext = plaintext.encode('utf-8')
    c_text1 = rsa_mod.encrypt(plaintext)
    c_text1 = c_text1.hex()
    #print("cipher after rsa: ", c_text1)

    #Caesar
    caesar = Caesar()
    caesar_key = 2203
    c_text_caesar = caesar.encryptCaesar(c_text1, caesar_key)
    #print("cipher after caesar: ", c_text_caesar)

    #ECB
    oracle = Oracle()
    oracle.set_target_message(c_text_caesar)
    ciphertext = oracle.initiate_encryption()
    # ciphertext_hex = ciphertext.hex()
    # print("ECB cipher is: ", ciphertext_hex)

    input_ciphertext = ciphertext
    print("Ciphertext after encrypting by BCR system: ", input_ciphertext.hex())

    #Decryption
    decrypt_time_s = time.time()
    ecb_decrypted_text = oracle.decrypt(input_ciphertext)
    caesar_decrypted_text = caesar.decryptCaesar(ecb_decrypted_text, caesar_key)
    caesar_decrypted_text = bytes.fromhex(caesar_decrypted_text)
    final_plaintext = rsa_mod.decrypt(caesar_decrypted_text, priv_key)
    print("Final_plaintext after decryption: ", final_plaintext.decode())
    decrypt_time_e = time.time()
    decrypt_time = decrypt_time_e - decrypt_time_s
    print("Decryption time: ", decrypt_time, "sec")

    attack_q = input("Start Attack?")
    if attack_q == 'n':
        exit()

    #Attack
    attack_time_s = time.time()
    plaintext=""
    token = oracle.get_token()
    for i in range(0, len(token), 16):
        oracle.set_target_message(token[i:i+16])
        attack = Attack(oracle)
    #start = time.time()
        plaintext += attack.start_attack_and_get_plaintext()
        #end = time.time()

    print("Attacked data after ecb attack: ", plaintext)
    print("Caesar ciphertext: ", c_text_caesar)
    possible = caesar.caesarAttack(plaintext)
    rsa_pl = ""
    hacked_d = rsa_mod.hack_RSA()
    print("hacked_d: ", hacked_d)
    hacked_priv_key = rsa_mod.get_private_key(hacked_d)
    print("Possible list: ", possible)
    for element in possible:
        try:
            x = bytes.fromhex(element)
            rsa_p = rsa_mod.decrypt(x, hacked_priv_key)
            rsa_pl = rsa_p.decode()
            #print("rsa_p", rsa_p)
            attack_time_e = time.time()
            break
        except(Exception):
            #print("Not a valid plain text")
            pass

    print("Original Plaintext: ",orig_plaintext)
    print("Plaintext after attack: ", rsa_pl)
    attack_time = attack_time_e - attack_time_s
    print("Decryption time: ",decrypt_time, "sec")
    print("Attack time: ",attack_time, "sec")

def test_2():
    input_set = ["qwertyuiop{}asdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewq"]
    for input in input_set:
        test_A(input)








plaintext = "nishanth"

#plaintext = "12345".encode('utf-8')
# rsa_mod = RSA()
# rsa_mod.generate_keys()
# priv_key = rsa_mod.get_private_key(rsa_mod.get_actual_d())
# c_text = rsa_mod.encrypt(plaintext)
# print(type(c_text))
#
# c_text_hex = c_text.hex()
# print("ciphertext: ", c_text)
# print("ciphertext after hex: ", c_text_hex)
#
# #p_text = rsa_mod.decrypt(c_text, priv_key)"""
# hacked_d = rsa_mod.hack_RSA()
# hacked_priv_key = rsa_mod.get_private_key(hacked_d)
# hacked_ptext = rsa_mod.decrypt(c_text, hacked_priv_key)
#
# print("Actual plaintext: ", plaintext, " derived plaintext is: ", hacked_ptext)
#
# caesar = Caesar()
# c_text_caesar = caesar.encryptCaesar(c_text_hex, 2203)
# print("cipher after caesar: ", c_text_caesar)
#
# caesar_p = caesar.decryptCaesar(c_text_caesar, 2203)
# #possible = caesar.frequencyAttack(c_text_caesar)
# possible = caesar.caesarAttack(c_text_caesar)
# print("decrypted_Caesar: ", caesar_p)
# print("possible: ", possible)
# x = bytes.fromhex(caesar_p)
# rsa_p = rsa_mod.decrypt(x, priv_key)
# print("rsa_p", rsa_p)
# #print("possible: ", possible)
#
#
# # print("plain after caesar: ", caesar_p)
# rsa_pl = ""
# for element in possible:
#     try:
#         x = bytes.fromhex(element)
#         rsa_p = rsa_mod.decrypt(x, priv_key)
#         rsa_pl = rsa_p.decode()
#         #print("rsa_p", rsa_p)
#         rsa_
#     except(Exception):
#         print("Not a valid plain text")
# print("RSA_P: ", rsa_pl)
#
# oracle = Oracle()
# oracle.set_target_message(c_text_caesar)
# ciphertext = oracle.initiate_encryption()
# print("ECB cipher is: ", ciphertext)
# p = oracle.decrypt(ciphertext)
# print("Decrpyted thing: ", p)
# caesar_text = caesar.decryptCaesar(p, 2203)
# x = bytes.fromhex(caesar_text)
# rsa_p = rsa_mod.decrypt(x, priv_key)
# print("rsa_p", rsa_p)

test_2()
