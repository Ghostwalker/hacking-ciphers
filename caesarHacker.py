# This program is meant to bruteforce through a Caesar  encoded Ciphertext


message = 'GUVF VF ZL FRPERG ZRFFNTR.'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
for key in range(len(LETTERS)):

    # Set translated to a blank string so that the
    # previous iteration's value  is cleared.
    translated = ''

    # The rest of the program is the same as the original Caesar program:

    # run the encryption or decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key

            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)

            # add number's symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # just add the symbol without encrypting or decrypting
            translated = translated + symbol

    # display the current key   tested   with its decryption
    print('Key #%s: %s' % (key, translated))
