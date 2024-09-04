#!/usr/bin/python

#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
#                    [====={ CRYPTO VENOM }=====]
#
#     | ATTENTION!: THIS SOFTWARE IS PART OF THE "CRYPTOVENOM FRAMEWORK" |
#
#              ( https://github.com/lockedbyte/cryptovenom )
#
#           << GNU PUBLIC LICENSE >>
#
#                               / CREATED BY LOCKEDBYTE /
#
#                  [ CONTACT => alejandro.guerrero.rodriguez2@gmail.com ]
#                  [ CONTACT => @LockedByte (Twitter) ]
#
#
# AND NOW...HERE THE CODE
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#


import base64
import base58
import binascii

BLOCK_SIZE = 8
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def text_to_bits(text, encoding='utf-8'):

    bits = bin(int(binascii.hexlify(text.encode(encoding)), 16))[2:]
    
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8'):

    n = int(bits, 2)
    
    return int2bytes(n).decode(encoding)

def int2bytes(i):

    hex_string = '%x' % i
    
    n = len(hex_string)
    
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def rc4(key, data):
    S = list(range(256))
    j = 0

    for i in list(range(256)):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    j = 0
    y = 0
    out = []

    for char in data:
        j = (j + 1) % 256
        y = (y + S[j]) % 256
        S[j], S[y] = S[y], S[j]
        
        version = 2

        if version == 2:
            out.append(unichr(ord(char) ^ S[(S[j] + S[y]) % 256]))

        if version == 3:
            out.append(chr(ord(char) ^ S[(S[j] + S[y]) % 256]))

    return ''.join(out)
        

def rc4cipher(importx, exportx, expfilepath, filepath, inputformat, passwd, raw, keyimport, outputformat):

    # REMEMBER!: THERE IS NO RC4ENCRYPT() AND RC4DECRYPT() FUNCTIONS CAUSE IS THE SAME:
        # ENCRYPT: ciphertext = rc4(key, cleartext)
        # DECRYPT: cleartext = rc4(key, ciphertext)

    if keyimport == 'base64':
    
        key = base64.b64decode(passwd)
        
    elif keyimport == 'raw':
    
        key = passwd 
    
    elif keyimport == 'base32':
    
        key = base64.b32decode(passwd)
    
    elif keyimport == 'base16':
    
        key = base64.b16decode(passwd)
    
    elif keyimport == 'base58':
    
        key = base58.b58decode(passwd)
    
    elif keyimport == 'base85':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif keyimport == 'hex':
    
        key = passwd.decode('hex')
    
    elif keyimport == 'dec':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif keyimport == 'octal':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif keyimport == 'binary':
    
        key = text_from_bits(passwd)
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        

    if importx == 'file':
    
        f = open(impfilepath, 'r')
        raw = f.read()
        f.close()
        
    elif importx == 'print':
    
        raw = raw
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    inp = raw


    if inputformat == 'base64':
    
        iput = base64.b64decode(inp)
    
    elif inputformat == 'base32':
    
        iput = base64.b32decode(inp)
    
    elif inputformat == 'base16':
    
        iput = base64.b16decode(inp)
    
    elif inputformat == 'base58':
    
        iput = base58.b58decode(inp)
    
    elif inputformat == 'base85':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif inputformat == 'hex':
    
        iput = inp.decode('hex')
    
    elif inputformat == 'dec':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif inputformat == 'octal':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif inputformat == 'binary':
    
        iput = text_from_bits(inp)
      
    elif inputformat == 'raw':
    
        iput = inp
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    out = rc4(key, iput.decode('utf-8'))
    
    out = out.encode('utf-8')
        
    if outputformat == 'base64':
    
        output = base64.b64encode(out)
        
    elif outputformat == 'raw':
    
        output = out
    
    elif outputformat == 'base32':
    
        output = base64.b32encode(out)
    
    elif outputformat == 'base16':
    
        output = base64.b16encode(out)
    
    elif outputformat == 'base58':
    
        output = base58.b58encode(out)
    
    elif outputformat == 'base85':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'hex':
    
        output = out.encode('hex').upper()
    
    elif outputformat == 'dec':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'octal':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'binary':
    
        output = text_to_bits(out)
        
    elif outputformat == 'raw':
    
        output = out
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        

    if exportx == 'file':
    
        f = open(outfilepath, 'w')
        f.write(output)
        f.close()
        return True
        
    elif exportx == 'print':
    
        return output
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
    
         
    



