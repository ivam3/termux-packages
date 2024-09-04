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

  
def printFence(fence):
    for rail in range(len(fence)):
        print ''.join(fence[rail])
    
def encryptFence(plain, rails, offset=0, debug=False):
    cipher = ''

    plain = '#'*offset + plain

    length = len(plain)
    fence = [['#']*length for _ in range(rails)]

    rail = 0
    for x in range(length):
        fence[rail][x] = plain[x]
        if rail >= rails-1:
            dr = -1
        elif rail <= 0:
            dr = 1
        rail += dr

    if debug:
        printFence(fence)

    for rail in range(rails):
        for x in range(length):
            if fence[rail][x] != '#':
                cipher += fence[rail][x]
    return cipher


def decryptFence(cipher, rails, offset=0, debug=False):
    plain = ''

    if offset:
        t = encryptFence('o'*offset + 'x'*len(cipher), rails)
        for i in range(len(t)):
            if(t[i] == 'o'):
                cipher = cipher[:i] + '#' + cipher[i:]
    
    length = len(cipher)
    fence = [['#']*length for _ in range(rails)]

    i = 0
    for rail in range(rails):
        p = (rail != (rails-1))
        x = rail
        while (x < length and i < length):
            fence[rail][x] = cipher[i]
            if p:
                x += 2*(rails - rail - 1)
            else:
                x += 2*rail
            if (rail != 0) and (rail != (rails-1)):
                p = not p
            i += 1

    if debug:
        printFence(fence)

    for i in range(length):
        for rail in range(rails):
            if fence[rail][i] != '#':
                plain += fence[rail][i]
    return plain

    

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
    
    

def railfenceencode(importx, infilepath, outfilepath, inputformat, exportx, raw, offset, rails):

    if importx == 'file':
    
        f = open(infilepath, 'r')
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
        
    elif inputformat == 'raw':
    
        iput = inp 
    
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
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    output = encryptFence(iput, rails, offset=offset, debug=False)

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
        
        
        
def railfencedecode(importx, infilepath, outfilepath, outputformat, exportx, raw, offset, rails):

    if importx == 'file':
    
        f = open(infilepath, 'r')
        raw = f.read()
        f.close()
        
    elif importx == 'print':
    
        raw = raw
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    out = decryptFence(raw, rails, offset=offset, debug=False)
    
    if outputformat == 'base64':
    
        output = base64.b64decode(out)
        
    elif outputformat == 'raw':
    
        output = out 
    
    elif outputformat == 'base32':
    
        output = base64.b32decode(out)
    
    elif outputformat == 'base16':
    
        output = base64.b16decode(out)
    
    elif outputformat == 'base58':
    
        output = base58.b58decode(out)
    
    elif outputformat == 'base85':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'hex':
    
        output = out.decode('hex')
    
    elif outputformat == 'dec':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'octal':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'binary':
    
        output = text_from_bits(out)
        
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

