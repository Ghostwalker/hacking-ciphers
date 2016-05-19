hacking-ciphers
#Copy-paste exercises for  Al Sweigart's book "Hacking Secret Ciphers with Python", might follow up with Zed Shaw's "Learn Python the Hard Way". Written for python 3


message = 'Three can keep a secret, if two of them are dead.'
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
