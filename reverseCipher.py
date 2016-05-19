# this program encrypts and decrypts a  plaintext by reverse ordering each of its characters

message = 'Three can keep a secret, if two of them are dead.' #the message variable stores your plaintext in the form of string 
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
