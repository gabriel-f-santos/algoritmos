#!/usr/bin/python3
#/tmp/cripto/cesar.py

def encrypt(text, slide):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + slide - 65) % 26 + 65)
        else:
            result += chr((ord(char) + slide - 97) % 26 + 97)
    return result

def decrypt(text, slide):
    text = text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for l in text:
        index = (alpha.find(l) - slide) % 26
        result += alpha[index]
    return result

frase = "ABCDEFZ"
print(f"Frase {frase}")
encrypted = encrypt("ABCDEFZ", 1)
print(f"Frase encriptada {encrypted}")
decrypted = decrypt(encrypted, 1)
print(f"Frase desencriptada {decrypted}")