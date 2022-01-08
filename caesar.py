
def encrypt(key,plaintext):
    ciphertext = ""
    key %= 26
    #YOUR CODE HERE
    for char in plaintext:
        if char != " ":
            code = (ord(char.upper()) - 65 + key) % 26
            ciphertext += chr((code+65))
        else:
            ciphertext += " "
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    key %= 26
    #YOUR CODE HERE
    for char in ciphertext:
        if char != " ":
            code = (ord(char.upper()) - 65 - key + 26) % 26
            plaintext += chr((code+65))
        else:
            plaintext += " "
    return plaintext



