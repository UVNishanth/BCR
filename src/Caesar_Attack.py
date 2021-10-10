class Caesar:
    def __init__(self):
        """self.freqs = {'A': 0.08167, 'N': 0.06749, 'B': 0.01492, 'O': 0.07507, 'C': 0.02782, 'P': 0.01929, 'D': 0.04253, 'Q': 0.00095,
                             'E': 0.12702, 'R': 0.05987, 'F': 0.02228, 'S': 0.06327, 'G': 0.02015, 'T': 0.09056, 'H': 0.06094, 'U': 0.02758,
                             'I': 0.06966, 'V': 0.00978, 'J': 0.00153, 'W': 0.0236, 'K': 0.00772, 'X': 0.0015, 'L': 0.04025, 'Y': 0.01974,
                             'M': 0.02406, 'Z': 0.00074}"""
        self.letters = 'abcdefghijklmnopqrstuvwxyz'

    def encryptCaesar(self, text, key):
        a_key = int(key / 100)
        # n_key = key % 100
        # text = text.lower()
        newtext = ""
        for c in text:
            if (c == ' '):
                newtext += ' '
                continue

            if (c.isnumeric()):
                new_c = int(c) - 3
                if (new_c < 0):
                    new_c = int(9 + new_c + 1)
                newtext += str(new_c)
            else:
                # c = c.lower()
                newtext += (chr((ord(c) - ord('a') + a_key) % 26 + ord('a')))
        return newtext

    def decryptCaesar(self, text, key):
        key = int(key / 100)
        newtext = ""
        for c in text:
            if (c == ' '):
                newtext += ' '
                continue
            if c.isnumeric():
                new_c = int(c) + 3
                if (new_c >= 10):
                    new_c = int(new_c - 9 - 1)
                newtext += str(new_c)
            else:
                # text = text.lower()
                newtext += chr((ord(c) - ord('a') + 26 - key) % 26 + ord('a'))
        return newtext

    def caesarAttack(self, text):
        letters = self.letters
        arr = []
        #return newtext
        for key in range(len(letters)):
            translated = ''
            for c in text:
                if (c == ' '):
                    translated += ' '
                    continue
                if c.isnumeric():
                    new_c = int(c) + 3
                    if (new_c >= 10):
                        new_c = int(new_c - 9 - 1)
                    translated += str(new_c)
                else:
                    # text = text.lower()
                    if c in letters:
                        num = letters.find(c)
                        num = num - key
                        if num < 0:
                            num = num + len(letters)
                        translated = translated + letters[num]
                    else:
                        translated = translated + c
            arr.append(translated)
            #print('Hacking key #%s: %s' % (key, translated))
        return arr
