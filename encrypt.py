alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Hi")
print("It's sentence and word to encrypt and decrypt")
stringToEncrypt = input("Write a sentence or word to encrypt(or decrypt) ")
stringToEncrypt = stringToEncrypt.upper()
shiftAmount = int(input("Write a number to encrypt(from 1 to 32) or decrypt(from -1 to -32) "))
encryptedString = ""
for currentCharacter in stringToEncrypt:
    position = alphabet.find(currentCharacter)
    newPosition = position + shiftAmount
    if currentCharacter in alphabet:
        encryptedString = encryptedString + alphabet[newPosition]
    else:
        encryptedString = encryptedString + currentCharacter
print("Your encrypted (or decrypted) sentence (or word) is",encryptedString,)