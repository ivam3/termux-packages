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
    

def runningkey(txt, key, encode=1):
    ltrs = [
        None, 'a', 'b',
        'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z']

    output = ""
    for i, l in enumerate(txt):
        if l == " ":
            output += " "
        else:
            current = ""
            key_ltr = key[i % len(key)]
            key_ltr_num = ltrs.index(key_ltr)
            txt_ltr_num = ltrs.index(l)
            if encode:
                output_ltr_num = txt_ltr_num + key_ltr_num
                output_ltr = ltrs[
                    output_ltr_num - 26
                    if output_ltr_num > 26 else output_ltr_num]
            else:
                output_ltr_num = txt_ltr_num - key_ltr_num
                output_ltr = ltrs[
                    txt_ltr_num + 26 - key_ltr_num
                    if txt_ltr_num <= key_ltr_num else txt_ltr_num - key_ltr_num]

            output += output_ltr
            current += (
                "key ltr num: %s - %s\n"
                "Plain ltr num: %s - %s\n"
                "Output: %s - %s\n\n") % (
                key_ltr, key_ltr_num,
                l, txt_ltr_num,
                output_ltr, output_ltr_num)


def runningkey2(txt, key, encode):
    output = ''
    for i in txt.split(" "):
        output += runningkey(i, key, encode)
        output += " "
    print(output)
     

def runningkeyencode(importx, infilepath, outfilepath, inputformat, exportx, key, raw):

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
        
    output = runningkey2(iput, key, 1)

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
        
        
        
def runningkeydecode(importx, infilepath, outfilepath, outputformat, exportx, key, raw):

    if importx == 'file':
    
        f = open(infilepath, 'r')
        raw = f.read()
        f.close()
        
    elif importx == 'print':
    
        raw = raw
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    out = runningkey2(raw, key, 0)
    
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


