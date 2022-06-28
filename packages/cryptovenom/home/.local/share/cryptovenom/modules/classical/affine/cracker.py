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

import re
from ngram_score import ngram_score
from pycipher import Affine
        
def break_affine(ctext, fitness):

    ctext = re.sub('[^A-Z]','',ctext.upper())
    scores = []
    for i in [1,3,5,7,9,11,15,17,19,21,23,25]:
        scores.extend([(fitness.score(Affine(i,j).decipher(ctext)),(i,j)) for j in range(0,25)])
    return max(scores)
  
def AffineCracker(ctext, ngram):
    fitness = ngram_score(ngram)
    max_key = break_affine(ctext, fitness)

    print('\033[1;32m[+]\033[0m Best candidate with key (a,b) = '+str(max_key[1])+':')
    print(Affine(max_key[1][0],max_key[1][1]).decipher(ctext))
    
    




