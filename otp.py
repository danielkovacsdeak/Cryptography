import string

def otp():
    '''
    One-time-pad encrypting program. Encode or decode your message
    with security key. 
    About one-time-pad: https://en.wikipedia.org/wiki/One-time_pad
    '''

    key = input('Enter your security key:')
    message = input('Enter your message:')
    
    codingType = input('If you want encoding type "e", if decode type "d":')
    while codingType not in ['e', 'd']:
        print('Invalid value. Try again.')
        codingType = input('If you want encoding type "e", if decode type "d":')
        
    if codingType == 'e':
        codingType = 1
    else:
        codingType = -1
        
    if len(key) < len(message):
        for i in range(len(message) - len(key)):
            key = key + key[i]
        
    lookup = string.printable
    result = ''
    i = 0
    
    for letter in message:
        result = result + lookup[(lookup.index(letter) + codingType * lookup.index(key[i])) % len(lookup)]
        i += 1
    return result
otp()