# aes_ecb_attack.py

import string
import time

class Attack:

    def __init__(self, oracle):
        self.chars = '0123456789!$%&\'()*=+,-./:;?@[\\]^_`{|}~ \t\n\r\x0b\x0cABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        self.oracle = oracle

    def start_attack_and_get_plaintext(self):
        display = True
        walkthru = True
        seeOracle = True
        timing =  False

        return self.attack(display, walkthru, seeOracle,  timing)

    # attack!
    # -------------------------------
    def attack(self, disp,walkthru=False, see_oracle = False, timing = False):
        first = True
        upper = 32
        # Max length of secret
        secret_len = 24
        len_init =  upper - len("data=")
        a_list = 'a' * len_init # list of a's

        known = a_list

        # If Walkthru, stop at each byte
        if walkthru:
            i = 0
            known_list = []
            # For each byte in the length of the max length of secret
            for i in range(secret_len):
                # the first byte doesn't give you information on secret just cycles through the a's
                #	so we don't display it
                if first:
                    known = self.get_next_byte(a_list, known, upper, False, walkthru, see_oracle, timing)
                    first = False
                else:
                    known = self.get_next_byte(a_list, known, upper, disp, walkthru, see_oracle, timing)
                a_list = a_list[0:-1]
                known_list += [known]

            # Print a summary of results
            print("Summary:\n")
            for i in known_list:
                if timing: time.sleep(.05)
                print("Known: ", i)

        # Else do all bytes at once
        else:
            for i in range(secret_len):
                known = self.get_next_byte(a_list, known, upper, disp, walkthru, see_oracle, timing)
                a_list = a_list[0:-1]

        # Print Result
        len_fin = len(a_list) +1
        result = known[len_fin:].split(",")[1]
        print("\nResult\n------------------------------\n", result,"\n")
        res =  result.split("=")[1].strip("X")
        print(res, "\n\n")
        return res



    # Brute force the next byte of the secret message
    # -------------------------------
    def get_next_byte(self, a_list, known, upper, disp, walkthru, see_oracle, timing=False):
        D = {}
        # Cycle through every character and record cipher texts
        for c in self.chars:
            # for c in range(256):
            print(known, c)
            # ch = c.to_bytes(1, 'big')
            curr = known[1:] + c
            encrypted = self.oracle.oracle(curr, disp, see_oracle, timing)
            second_block = encrypted[16:upper]
            D[second_block] = c

        # Cipher text with correct next character
        # obtained my shortening the input by one character
        correct_curr = self.oracle.oracle(a_list, disp, see_oracle, timing)[16:upper]

        # If the correct cipher text is in the dictionary keys,
        # then it's corresponding value is the next correct char
        if correct_curr in D.keys():
            true_char = D[correct_curr]
            # Add next character to result
            result = known[1:] + true_char

        # If walkthru/timing display/pause
        if walkthru:
            if timing: time.sleep(.3)
            self.display_round(known, true_char, result)
        print(known, c)
        return result

    # For display purposes
    # -------------------------------

    def display_round(self, known, true_char, result):
        print("\n\nCall oracle on the following for every char '?':\n", known[1:], "?")
        print("Result \n", result)
        print("True character: ", true_char, "\n")
