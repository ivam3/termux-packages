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


import sys
import math

def prime_factorize(n):
    factors = []
    number = math.fabs(n)
    while number > 1:
        factor = get_next_prime_factor(number)
        factors.append(factor)
        number /= factor
    if n < -1:
        factors[0] = -factors[0]
    return tuple(factors)
    
def get_next_prime_factor(n):
    if n % 2 == 0:
        return 2
    for x in range(3, int(math.ceil(math.sqrt(n)) + 1), 2):
        if n % x == 0:
            return x
    return int(n)
