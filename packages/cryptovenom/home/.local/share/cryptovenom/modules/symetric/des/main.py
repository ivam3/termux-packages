#!/usr/bin/python

#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
#                    [====={ CRYPTO VENOM }=====]
#
#     | ATTENTION!: THIS SOFTWARE IS PART OF CRYPTOVENOM FRAMEWORK |
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


import sys
import base64
from Crypto import Random
from Crypto.Cipher import DES
import base58
import binascii


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

BLOCK_SIZE = 8
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def encryptDes(destype, importx, impfilepath, export, filepath, outputformat, ivtype, iv, passwd, raw, keyimport):


    if keyimport == 'base64':
    
        key = base64.b64decode(passwd)
    
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
        
    elif keyimport == 'raw':
    
        key = passwd 
               
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
        
    raw = pad(raw)
    
    if len(passwd) == 8:
    
        key = passwd
            
    else:
        
        print('\033[1;31m[-]\033[0m DES Key must be 8 bytes long')

    if ivtype == 'randomstart':
    
        iv = Random.new().read(DES.block_size)
        sadd = iv
        eadd = ''
    
    elif ivtype == 'randomend':
    
        iv = Random.new().read(DES.block_size)
        sadd = ''
        eadd = iv
    
    elif ivtype == 'custom':
    
        iv = iv
        sadd = iv
        eadd = ''
    
    elif ivtype == 'noiv':
    
        sadd = ''
        eadd = ''
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False

    if destype == 'ecb':
        
        cipher = DES.new(key, DES.MODE_ECB)
    
    
    elif destype == 'cbc':
    
        cipher = DES.new(key, DES.MODE_CBC, iv)
        
    elif destype == 'ofb':
    
        cipher = DES.new(key, DES.MODE_OFB, iv)
    
    elif destype == 'ocb':
    
        cipher = DES.new(key, DES.MODE_OCB, iv)
    
    elif destype == 'ctr':
    
        cipher = DES.new(key, DES.MODE_CTR)
    
    elif destype == 'cfb':
    
        cipher = DES.new(key, DES.MODE_CFB, iv)
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    out = cipher.encrypt(raw)
    
    out = sadd + out + eadd
        
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
    
        output = out.encode('hex')
    
    elif outputformat == 'dec':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'octal':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'binary':
    
        output = text_to_bits(out)
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    if export == 'file':
    
        filename = open(filepath, 'w')
        filename.write(output)
        filename.close()
        
        return True
        
    elif export == 'print':
    
        return output
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
        

def decryptDes(destype, importx, filepath, export, expfilepath, inputformat, ivtype, iv, passwd, raw):


    if importx == 'file':
    
        f = open(filepath, 'r')
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
        
    if len(passwd) == 8:
    
        key = passwd
            
    else:
        
        print('\033[1;31m[-]\033[0m DES Key must be 8 bytes long')

    if ivtype == 'randomstart':
    
        iv = iput[:8]
        iput = iput[8:]
    
    elif ivtype == 'randomend':
    
        iv = iput[-8:]
        iput = iput[:-8]
    
    elif ivtype == 'custom':
    
        iv = iv
        iput = iput
    
    elif ivtype == 'noiv':
    
        iv = ''
        iput = iput
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False

    if destype == 'ecb':
        
        cipher = DES.new(key, DES.MODE_ECB)
        
    elif destype == 'ofb':
    
        cipher = DES.new(key, DES.MODE_OFB, iv)
    
    
    elif destype == 'cbc':
    
        cipher = DES.new(key, DES.MODE_CBC, iv)
    
    elif destype == 'ocb':
    
        cipher = DES.new(key, DES.MODE_OCB, iv)
    
    elif destype == 'ctr':
    
        cipher = DES.new(key, DES.MODE_CTR)
    
    elif destype == 'cfb':
    
        cipher = DES.new(key, DES.MODE_CFB, iv)
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    out = cipher.decrypt(iput)
    
    out = unpad(out)
    
    if export == 'file':
    
        filename = open(expfilepath, 'w')
        filename.write(out)
        filename.close()
        
        return True
        
    elif export == 'print':
    
        return out
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
    
    

