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

import random

def Abp(A, b, p):

    K = (A ** b) % p
    
    return K
        

def Bap(B, a, p):

    K = (B ** a) % p
    
    return K


def abgp(a, b, g, p):

    A = (g ** a) % p
    B = (g ** b) % p
    
    K = (B ** a) % p
    
    return K


def genkey(mink, maxk, ming, maxg):

    g = random.randint(ming, maxg)
    p = random.randint(maxg, maxg + 200)
    a = random.randint(mink, maxk)
    
    values = [g,p,a]
    
    return values


