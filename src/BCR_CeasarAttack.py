freqs = {'a': 0.08167, 'n': 0.06749, 'b': 0.01492, 'o': 0.07507, 'c': 0.02782, 'p': 0.01929, 'd': 0.04253, 'q': 0.00095,
         'e': 0.12702, 'r': 0.05987, 'f': 0.02228, 's': 0.06327, 'g': 0.02015, 't': 0.09056, 'h': 0.06094, 'u': 0.02758,
         'i': 0.06966, 'v': 0.00978, 'j': 0.00153, 'w': 0.0236, 'k': 0.00772, 'x': 0.0015, 'l': 0.04025, 'y': 0.01974,
         'm': 0.02406, 'z': 0.00074}


def encryptCaesar(text, key):
    a_key = int(key / 100)
    #n_key = key % 100
    #text = text.lower()
    newtext = ""
    for c in text:
        if (c == ' '):
            newtext += ' '
            continue

        if (c.isnumeric() ):
            new_c = int(c) - 3
            if (new_c < 0):
                new_c = int(9 + new_c + 1)
            newtext += str(new_c)
        else:
            c = c.lower()
            newtext += (chr((ord(c) - ord('a') + a_key) % 26 + ord('a')))
    return newtext


def decryptCaesar(text, key):

    newtext = ""
    for c in text:
        if (c == ' '):
            newtext += ' '
            continue
        if c.isnumeric() :
            new_c = int(c) + 3
            if (new_c >= 10):
                new_c = int(new_c - 9 - 1)
            newtext += str(new_c)
        else:
            text = text.lower()
            newtext += chr((ord(c) - ord('a') + 26 - key) % 26 + ord('a'))
    return newtext


def frequencyCounts(text):
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


def frequencyAttack():
    minScore = 10000
    possibleKey = 0
    allScores = {}
    for key in range(26):
        decryption = decryptCaesar(ciphertext, key)

        counts = frequencyCounts(decryption)
        allScores[key] = findScore(counts)

        if (allScores[key] < minScore):
            minScore = allScores[key]
            possibleKey = key
    print("Most possible key is :  " + str(possibleKey))
    print("Corresponding decrypted ciphertext : " + decryptCaesar(ciphertext, possibleKey))
    allScores = {k: v for k, v in sorted(allScores.items(), key=lambda item: item[1])}
    print("\n Next top 10 possible decryptions : ")
    start = 0
    for i in allScores:
        if (start == 0):
            start = 1
            continue
        print(decryptCaesar(ciphertext, i))
        start += 1
        if (start == 10):
            break


def findScore(counts):
    score = 0
    for i in range(26):
        letter = chr(i + ord('a'))
        if letter not in counts:
            counts[letter] = 0.0
        score += abs(freqs[letter] - counts[letter])
    return score


#message = "Meet me at serpentine tonight with the requested package"
# message = "The quick brown fox jumps over the lazy dog"

message ="573IEJ169J65HJHI8H95412J0F434J93E7I4F9E9I9E9F545177142J"
key = 2203
ciphertext = encryptCaesar(message, key)

print("Given cipher text : " + ciphertext)
frequencyAttack()