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


from ngram_score import ngram_score
from pycipher import Vigenere
import re
from itertools import permutations

class nbest(object):
    def __init__(self,N=1000):
        self.store = []
        self.N = N
        
    def add(self,item):
        self.store.append(item)
        self.store.sort(reverse=True)
        self.store = self.store[:self.N]
    
    def __getitem__(self,k):
        return self.store[k]

    def __len__(self):
        return len(self.store)



def VigenereCracker(ctext, q1gram, t1gram):

    qgram = ngram_score(q1gram)
    trigram = ngram_score(t1gram)
    ctext = re.sub(r'[^A-Z]','',ctext.upper())
    N = 100
    for KLEN in range(3,20):
        rec = nbest(N)

        for i in permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ',3):
            key = ''.join(i) + 'A'*(KLEN-len(i))
            pt = Vigenere(key).decipher(ctext)
            score = 0
            for j in range(0,len(ctext),KLEN):
                score += trigram.score(pt[j:j+3])
            rec.add((score,''.join(i),pt[:30]))

        next_rec = nbest(N)
        for i in range(0,KLEN-3):
            for k in xrange(N):
                for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    key = rec[k][1] + c
                    fullkey = key + 'A'*(KLEN-len(key))
                    pt = Vigenere(fullkey).decipher(ctext)
                    score = 0
                    for j in range(0,len(ctext),KLEN):
                        score += qgram.score(pt[j:j+len(key)])
                    next_rec.add((score,key,pt[:30]))
            rec = next_rec
            next_rec = nbest(N)
        bestkey = rec[0][1]
        pt = Vigenere(bestkey).decipher(ctext)
        bestscore = qgram.score(pt)
        for i in range(N):
            pt = Vigenere(rec[i][1]).decipher(ctext)
            score = qgram.score(pt)
            if score > bestscore:
                bestkey = rec[i][1]
                bestscore = score       
        print('\033[1;34m[*]\033[0m Score = ' + str(bestscore) + ' ; Iteraction = ' + str(KLEN) + ' ; Key = ' + str(bestkey) + ' ; Out = ' + Vigenere(bestkey).decipher(ctext))
    

