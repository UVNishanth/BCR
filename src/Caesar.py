"""freqs = {'a': 0.08167, 'n': 0.06749, 'b': 0.01492, 'o': 0.07507, 'c': 0.02782, 'p': 0.01929, 'd': 0.04253, 'q': 0.00095,
         'e': 0.12702, 'r': 0.05987, 'f': 0.02228, 's': 0.06327, 'g': 0.02015, 't': 0.09056, 'h': 0.06094, 'u': 0.02758,
         'i': 0.06966, 'v': 0.00978, 'j': 0.00153, 'w': 0.0236, 'k': 0.00772, 'x': 0.0015, 'l': 0.04025, 'y': 0.01974,
         'm': 0.02406, 'z': 0.00074}"""

class Caesar:
    def __init__(self):
        self.freqs = {'A': 0.08167, 'N': 0.06749, 'B': 0.01492, 'O': 0.07507, 'C': 0.02782, 'P': 0.01929, 'D': 0.04253, 'Q': 0.00095,
                             'E': 0.12702, 'R': 0.05987, 'F': 0.02228, 'S': 0.06327, 'G': 0.02015, 'T': 0.09056, 'H': 0.06094, 'U': 0.02758,
                             'I': 0.06966, 'V': 0.00978, 'J': 0.00153, 'W': 0.0236, 'K': 0.00772, 'X': 0.0015, 'L': 0.04025, 'Y': 0.01974,
                             'M': 0.02406, 'Z': 0.00074}

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
                newtext += (chr((ord(c) - ord('A') + a_key) % 26 + ord('A')))
        return newtext

    def decryptCaesar(self, text, key):

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
                newtext += chr((ord(c) - ord('A') + 26 - key) % 26 + ord('A'))
        return newtext

    def frequencyCounts(self, text):
        counts = {}
        total = 0
        for i in text:
            if i == ' ':
                continue
            if i.isnumeric():
                continue
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
            total += 1
        for i in counts:
            counts[i] = float(counts[i]) / float(total)

        return counts

    def frequencyAttack(self, ciphertext):
        minScore = 10000
        possibleKey = 0
        allScores = {}
        for key in range(26):
            decryption = self.decryptCaesar(ciphertext, key)

            counts = self.frequencyCounts(decryption)
            allScores[key] = self.findScore(counts)

            if (allScores[key] < minScore):
                minScore = allScores[key]
                possibleKey = key
        print("Most possible key is :  " + str(possibleKey))
        print("Corresponding decrypted ciphertext : " + self.decryptCaesar(ciphertext, possibleKey))
        allScores = {k: v for k, v in sorted(allScores.items(), key=lambda item: item[1])}
        print("\n Next top 10 possible decryptions : ")
        start = 0
        for i in allScores:
            if (start == 0):
                start = 1
                continue
            print(self.decryptCaesar(ciphertext, i))
            start += 1
            if (start == 10):
                break

    def findScore(self, counts):
        score = 0
        for i in range(26):
            letter = chr(i + ord('A'))
            if letter not in counts:
                counts[letter] = 0.0
            score += abs(self.freqs[letter] - counts[letter])
        return score
