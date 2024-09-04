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

from pycipher import Playfair

def PlayfairBF(ctext, dictionary):

    f = open(dictionary, 'r')
    keys = f.readlines()
    
    for i in keys:
        try:
            out = Plaifair(key=i[:-1]).decipher(ctext)
            print('\033[1;34m[*]\033[0m Key = ' + i[:-1] + ' ; Out = ' + out)     
        except:
            print('\033[1;34m[*]\033[0m Key = ' + i[:-1] + ' ; Err.: KeyError')
        
    print('\033[1;32m[+]\033[0m Brute Force finished.')
    
