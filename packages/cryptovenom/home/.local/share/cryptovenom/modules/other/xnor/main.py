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

def XNOR(a, b):
    A = []
    B = []
    C = []
    for ax in a:
        A.append(ax)
        
    for bx in b:
        B.append(bx)

    if len(A) == len(B):
    
        for i in range(len(A)):
        
            if A[i] == '0' and B[i] == '1':
            
                C.append('0')
                
            elif A[i] == '1' and B[i] == '0':
            
                C.append('0')
                
            elif A[i] == '0' and B[i] == '0':
            
                C.append('1')
                
            elif A[i] == '1' and B[i] == '1':
            
                C.append('1')
                
    out = ''
    for i in C:
        out += i
        
    print('\033[1;32m[+]\033[0m ' + a + ' XNOR ' + b + ' = ' + out)
    
        
            
