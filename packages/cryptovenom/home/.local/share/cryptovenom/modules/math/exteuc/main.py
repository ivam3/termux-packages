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

import gmpy2

def EEA(n1, n2):
    print('x*y == 1 (mod p)')
    print('y = invmod(x, p)')
    print('\n\033[1;34m[*]\033[0m Calculating...\n')
    n3 = gmpy2.invert(n1, n2)
    n3 = str(n3)
    n3 = n3.replace('mpz(', '')
    n3 = n3.replace(')', '')
    print('\033[1;34m[*]\033[0m ' + str(n1) + ' * ' + str(n2) + ' == 1 (mod ' + str(n2) + ')')
    print('\033[1;32m[+]\033[0m invmod(' + str(n1) + ', ' + str(n2) + ') = ' + str(n3))
    

