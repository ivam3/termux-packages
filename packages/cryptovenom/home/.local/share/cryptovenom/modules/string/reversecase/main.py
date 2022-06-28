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


def reversecase(method, inpath, outpath, string):

    if method == 'file':
    
        f = open(inpath, 'r')
        string = f.read()
        f.close()
        
        outstr = ''
        for i in string:
            if i.isupper():
                outstr = outstr + i.lower()
            else:
                outstr = outstr + i.upper()
        f2 = open(outpath, 'w')
        f2.write(outstr)
        f2.close()
        return True     
    
    elif method == 'text':
    
        outstr = ''
        for i in string:
            if i.isupper():
                outstr = outstr + i.lower()
            else:
                outstr = outstr + i.upper()
        return outstr

            
            

