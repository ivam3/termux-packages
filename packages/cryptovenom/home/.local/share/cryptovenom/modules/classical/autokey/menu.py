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
from cracker import *
from bruteforce import *

print '''

-=[OPTIONS]=-

   1) Encrypt
   2) Decrypt
   3) Cracker
   4) Brute Force
   
'''

opt = raw_input('\033[1;34m[=]\033[0m Option: ')


if opt == '1':


    opt2 = raw_input('\033[1;34m[=]\033[0m [F]ile or [T]ext: ')
    
    if opt2 == 'f' or opt2 == 'F':
    
        importx = 'file'
        exportx = 'file'
        
        text = ''
        
        infile = raw_input('\033[1;34m[=]\033[0m Input file path: ')
        outfile = raw_input('\033[1;34m[=]\033[0m Output file path: ')
    
    
    elif opt2 == 't' or opt2 == 'T':
    
        importx = 'print'
        exportx = 'print'
        infile = ''
        outfile = ''
        
        text = raw_input('\033[1;34m[=]\033[0m Text: ')
    
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown option')
        exit()
        
    format1 = raw_input('\033[1;34m[=]\033[0m Input format (Eg.: raw or base64): ')
    
    key = raw_input('\033[1;34m[=]\033[0m Key: ')
    
    out = autokeyencode(importx, infile, outfile, format1,  exportx, text, key)
    
    print('\033[1;32m[+]\033[0m Out = ' + str(out))
    print('\033[1;32m[+]\033[0m All done!')


elif opt == '2':


    opt2 = raw_input('\033[1;34m[=]\033[0m [F]ile or [T]ext: ')
    
    if opt2 == 'f' or opt2 == 'F':
    
        importx = 'file'
        exportx = 'file'
        
        text = ''
        
        infile = raw_input('\033[1;34m[=]\033[0m Input file path: ')
        outfile = raw_input('\033[1;34m[=]\033[0m Output file path: ')
    
    
    elif opt2 == 't' or opt2 == 'T':
    
        importx = 'print'
        exportx = 'print'
        infile = ''
        outfile = ''
        
        text = raw_input('\033[1;34m[=]\033[0m Text: ')
    
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown option')
        exit()
        
    format1 = raw_input('\033[1;34m[=]\033[0m Output format (Eg.: raw or base64): ')
    key = raw_input('\033[1;34m[=]\033[0m Key: ')
    
    out = autokeydecode(importx, infile, outfile, format1,  exportx, text, key)
    
    print('\033[1;32m[+]\033[0m Out = ' + str(out))
    print('\033[1;32m[+]\033[0m All done!')
    
elif opt == '3':

    opt2 = raw_input('\033[1;34m[=]\033[0m [F]ile or [T]ext: ')
    
    if opt2 == 'f' or opt2 == 'F':
        
        infile = raw_input('\033[1;34m[=]\033[0m Input file path: ')
        
        text = open(infile, 'r').read()
    
    
    elif opt2 == 't' or opt2 == 'T':
        
        text = raw_input('\033[1;34m[=]\033[0m Text: ')
    
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown option')
        exit()
        
    ngram1 = raw_input('\033[1;34m[=]\033[0m Quadram Path: ')
    ngram2 = raw_input('\033[1;34m[=]\033[0m Trigram Path: ')
    
    AutokeyCracker(text, ngram1, ngram2)
    
elif opt == '4':

    opt2 = raw_input('\033[1;34m[=]\033[0m [F]ile or [T]ext: ')
    
    if opt2 == 'f' or opt2 == 'F':
        
        infile = raw_input('\033[1;34m[=]\033[0m Input file path: ')
        
        text = open(infile, 'r').read()
    
    
    elif opt2 == 't' or opt2 == 'T':
        
        text = raw_input('\033[1;34m[=]\033[0m Text: ')
    
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown option')
        exit()
        
    dic = raw_input('\033[1;34m[=]\033[0m Wordlist Path: ')
    
    opt = raw_input('\033[1;34m[=]\033[0m Do you have known text? [y/N]: ')
    
    if opt == 'y' or opt == 'Y':
    
        ch = 'True'
        ch2 = raw_input('\033[1;34m[=]\033[0m Known-Text: ')
    
    elif opt == 'n' or opt == 'N':
    
        ch = 'False'
        ch2 = ''
    
    else:
        print('\033[1;31m[-]\033[0m Unknown option')
        exit()
    
    AutokeyBF(text, dic, ch, ch2)

else:

    print('\033[1;31m[-]\033[0m Unknown option')
    exit()
