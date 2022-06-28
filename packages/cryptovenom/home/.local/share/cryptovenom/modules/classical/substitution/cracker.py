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

from pycipher import SimpleSubstitution as SimpleSub
import random
import re
from ngram_score import ngram_score


def SubsCracker(ctext, ngram):

    fitness = ngram_score(ngram)

    ctext = re.sub('[^A-Z]','',ctext.upper())

    maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    maxscore = -99e9
    parentscore,parentkey = maxscore,maxkey[:]
    i = 0
    print('\033[1;34m[*]\033[0m Cracking the cipher. This might take a while...')
    while 1:
        i = i+1
        random.shuffle(parentkey)
        deciphered = SimpleSub(parentkey).decipher(ctext)
        parentscore = fitness.score(deciphered)
        count = 0
        while count < 1000:
            a = random.randint(0,25)
            b = random.randint(0,25)
            child = parentkey[:]
            child[a],child[b] = child[b],child[a]
            deciphered = SimpleSub(child).decipher(ctext)
            score = fitness.score(deciphered)
            if score > parentscore:
                parentscore = score
                parentkey = child[:]
                count = 0
            count = count+1
        if parentscore>maxscore:
            maxscore,maxkey = parentscore,parentkey[:]
            print('\n\033[1;34m[*]\033[0m Best score so far: ' + str(maxscore) + ' on iteration ' + str(i))
            ss = SimpleSub(maxkey)
            print('    \033[1;32m[+]\033[0m Best key: '+''.join(maxkey))
            print('    \033[1;32m[+]\033[0m Plaintext: '+ss.decipher(ctext))
            


