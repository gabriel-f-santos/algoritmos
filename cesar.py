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

print(encrypt("ABCDEFZ", 1))