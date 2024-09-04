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

n1 = raw_input('\033[1;34m[=]\033[0m Base (x): ')
n2 = raw_input('\033[1;34m[=]\033[0m Exponent (n): ')
print('\033[1;34m[*]\033[0m f(x) = x ** n')
n3 = fast_exp(int(n1),int(n2))

print('\033[1;32m[+]\033[0m f(x) = ' + str(n3))
