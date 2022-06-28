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

def blockreverse(method, inpath, outpath, string, delimiter, revblocks):

    if method == 'file':
    
        f = open(inpath, 'r')
        string = f.read()
        f.close()

        if revblocks:
            string2 = string.split(delimiter)
            outstr = ''
            for i in range(len(string2)):
                outstr = outstr + string2[(len(string2) - 1) - i][::-1] + delimiter
            outstr = outstr[:-len(delimiter)]
        else:
            string2 = string.split(delimiter)
            outstr = ''
            for i in string2:
                outstr = outstr + i[::-1] + delimiter
            outstr = outstr[:-len(delimiter)]
            
        f2 = open(outpath, 'w')
        f2.write(outstr)
        f2.close()
        return True
    
    elif method == 'text':
    
        if revblocks:
            string2 = string.split(delimiter)
            outstr = ''
            for i in range(len(string2)):
                outstr = outstr + string2[(len(string2) - 1) - i][::-1] + delimiter
            return outstr[:-len(delimiter)]
        else:
            string2 = string.split(delimiter)
            outstr = ''
            for i in string2:
                outstr = outstr + i[::-1] + delimiter
            return outstr[:-len(delimiter)]
    
    
