def encrypt(key,plaintext):
    ciphertext = ""
    key %= 26
    #YOUR CODE HERE
    for char in plaintext:
        if char.isalpha():
            code = (ord(char.upper()) - 65 + key) % 26
            ciphertext += chr((code+65))
        else:
            ciphertext += char
    return ciphertext

def decrypt(key,ciphertext):
    plaintext = encrypt(-key, ciphertext)
    return plaintext