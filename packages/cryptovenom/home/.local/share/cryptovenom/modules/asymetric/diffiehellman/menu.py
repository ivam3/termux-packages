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

-=[OPTIONS:Asymetric:DH]=-

   1) Generate Bob/Alice values (Just from one side)
   2) Get Key given A, b and p
   3) Get Key given B, a and p
   4) Get Key given a, b, g and p
   
  99) Exit
  
'''

opt = raw_input('\033[1;34m[=]\033[0m Option: ')

if opt == '99':

    print('\033[1;34m[*]\033[0m Exiting...')
    exit()
    
elif opt == '1':

    mink = raw_input('\033[1;34m[=]\033[0m Minimum Key Value: ')
    maxk = raw_input('\033[1;34m[=]\033[0m Maximum Key Value: ')
    ming = raw_input('\033[1;34m[=]\033[0m Minimum g Value: ')
    maxg = raw_input('\033[1;34m[=]\033[0m Maximum g Value: ')
    print('\033[1;34m[*]\033[0m Generating values...')
    keys = genkey(int(mink), int(maxk), int(ming), int(maxg))
    
    print('\t\033[1;32m[+]\033[0m g = ' + str(keys[0]))
    print('\t\033[1;32m[+]\033[0m p = ' + str(keys[1]))
    print('\t\033[1;32m[+]\033[0m a = ' + str(keys[2]))

elif opt == '2':

    A = raw_input('\033[1;34m[=]\033[0m A Value: ')
    b = raw_input('\033[1;34m[=]\033[0m b Value: ')
    p = raw_input('\033[1;34m[=]\033[0m p Value: ')
    print('\033[1;34m[*]\033[0m Getting key...')
    k = Abp(int(A), int(b), int(p))
    
    print('\t\033[1;32m[+]\033[0m K = ' + str(k))

elif opt == '3':

    B = raw_input('\033[1;34m[=]\033[0m B Value: ')
    a = raw_input('\033[1;34m[=]\033[0m a Value: ')
    p = raw_input('\033[1;34m[=]\033[0m p Value: ')
    print('\033[1;34m[*]\033[0m Getting key...')
    k = Bap(int(B), int(a), int(p))
    
    print('\t\033[1;32m[+]\033[0m K = ' + str(k))

elif opt == '4':

    a = raw_input('\033[1;34m[=]\033[0m a Value: ')
    b = raw_input('\033[1;34m[=]\033[0m b Value: ')
    g = raw_input('\033[1;34m[=]\033[0m g Value: ')
    p = raw_input('\033[1;34m[=]\033[0m p Value: ')
    print('\033[1;34m[*]\033[0m Getting key...')
    k = abgp(int(a), int(b), int(g), int(p))
    
    print('\t\033[1;32m[+]\033[0m K = ' + str(k))

else:

    print('\033[1;31m[-]\033[0m Unknown option')
    exit()

