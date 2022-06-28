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

from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA
from Crypto.Util.number import *
from Crypto.Util import asn1


def genKeys(bits):

    key = DSA.generate(1024)
    seq = asn1.DerSequence()
    seq[:] = [ 0, key.p, key.q, key.g, key.y, key.x ]
    k2 = "-----BEGIN DSA PRIVATE KEY-----\n%s-----END DSA PRIVATE KEY-----" % seq.encode().encode("base64")
    return k2


def verifyMsg(text, imported_key, sig):

    seq2 = asn1.DerSequence()
    data = '\n'.join(imported_key.strip().split('\n')[1:-1]).decode('base64')
    seq2.decode(data)
    p, q, g, y, x = seq2[1:]

    key2 = DSA.construct((y, g, p, q, x))
    
    k1 = random.StrongRandom().randint(1,key2.q-1)

    h = SHA.new(text).digest()

    a = key2.verify(h, sig)
    
    return a

def signMsg(text, imported_key):

    seq2 = asn1.DerSequence()
    data = '\n'.join(imported_key.strip().split('\n')[1:-1]).decode('base64')
    seq2.decode(data)
    p, q, g, y, x = seq2[1:]

    key2 = DSA.construct((y, g, p, q, x))
    
    k1 = random.StrongRandom().randint(1,key2.q-1)

    h = SHA.new(text).digest()

    sig = key2.sign(h, k1)
    
    return sig
    
    

