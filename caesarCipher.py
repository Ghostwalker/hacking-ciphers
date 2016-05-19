# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
#this program can encrypt a plaintext or decrypt a cryptogram by using the simple algorithm devised by Julius Caesar


# the string to be encrypted or decrypted
message = 'This is my secret message.'

# the encryption/decryption key
key = 13

#  select a mode
mode = 'encrypt' # set to 'encrypt' or 'decrypt'

# a string of characters that can be decoded/encoded
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# stores the encrypted or the decrypted form of the message
translated = ''

# capitalize the string in message
message = message.upper()

# run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        # get the encrypted (or decrypted) number for this symbol
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # if num is larger than the length of
        # LETTERS or less than 0 it wraps around 
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # add encrypted or decrypted number's symbol at the end of translated
        translated = translated + LETTERS[num]

    else:
        # just add the symbol without encrypting or decrypting
        translated = translated + symbol

# print the encrypted or the decrypted string to the screen
print(translated)

