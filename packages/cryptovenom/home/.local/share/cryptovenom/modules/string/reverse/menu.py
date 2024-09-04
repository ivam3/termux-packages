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

method = raw_input('\033[1;34m[=]\033[0m [F]ile Or [T]ext: ')

if method == 'f' or method == 'F':

    m = 'file'
    inpath = raw_input('\033[1;34m[=]\033[0m Input path: ')
    
    string = open(inpath, 'r').read()
    
    outpath = raw_input('\033[1;34m[=]\033[0m Output path: ')

elif method == 't' or method == 'T':

    m = 'text'
    string = raw_input('\033[1;34m[=]\033[0m Text: ')
    inpath = ''
    outpath = ''


else:

    print('\033[1;31m[-]\033[0m Unknown option')
    exit()
    
out = reverse(m, inpath, outpath, string)

print('\033[1;32m[+]\033[0m Out = ' + str(out))

print('\033[1;32m[+]\033[0m String reversed successfully!')

