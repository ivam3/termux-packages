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

from main import *

print '''

-=[OPTIONS:Asymetric:DSA]=-

   1) Generate Keys
   2) Sign Message
   3) Verify Message
   
  99) Exit

'''

opt = raw_input('\033[1;34m[=]\033[0m Option: ')

if opt == '99':

    print('\033[1;34m[*]\033[0m Exiting...')
    exit()

elif opt == '1':

    bits = raw_input('\033[1;34m[=]\033[0m Key Bits: ')
    
    out = genKeys(int(bits))
    
    print(out)
    print('\033[1;32m[+]\033[0m All done!')

elif opt == '2':

    op = raw_input('\033[1;34m[=]\033[0m [F]ile or [T]ext: ')
    
    if op == 't' or op == 'T':
    
        text = raw_input('\033[1;34m[=]\033[0m Message: ')
    
    elif op == 'f' or op == 'F':
    
        fp = raw_input('\033[1;34m[=]\033[0m File path: ')
        
        text = open(fp, 'r').read()
    
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown option')
        exit()
        
    k = raw_input('\033[1;34m[=]\033[0m Key File: ')
    
    key = open(k, 'r').read()
        
    out = signMsg(text, key)
    
    print('\033[1;32m[+]\033[0m Signature: ' + str(out))

elif opt == '3':

    op = raw_input('\033[1;34m[=]\033[0m [F]ile or [T]ext: ')
    
    if op == 't' or op == 'T':
    
        text = raw_input('\033[1;34m[=]\033[0m Message: ')
    
    elif op == 'f' or op == 'F':
    
        fp = raw_input('\033[1;34m[=]\033[0m File path: ')
        
        text = open(fp, 'r').read()
    
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown option')
        exit()
        
    k = raw_input('\033[1;34m[=]\033[0m Key File: ')
    
    sign1 = raw_input('\033[1;34m[=]\033[0m Number 1: ')
    sign2 = raw_input('\033[1;34m[=]\033[0m Number 2: ')
    
    tps = [int(sign1), int(sign2)]
    
    key = open(k, 'r').read()
        
    out = verifyMsg(text, key, tps)
    
    if out:
    
        print('\033[1;32m[+]\033[0m Valid signature!')
        
    else:
        
        print('\033[1;31m[-]\033[0m Signature is wrong!')

else:

    print('\033[1;31m[-]\033[0m Unknown option')
    exit()

