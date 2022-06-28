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
from Crypto.Util.number import *

print '''

-[MENU:Asymmetric:RSA]-

   1) Generate RSA Keys
   2) RSA Encrypt
   3) RSA Decrypt
   4) RSA Sign Message
   5) RSA Verify Signature
   6) Extract Public Key Parameters
   7) Extract Private Key Parameters
   8) Embed Public Key Parameters
   9) Embed Private Key Parameters
  10) Generate Numeric Keys (Guided RSA Internals)
  11) Decrypt Given p,q,e,c
  12) Decrypt Given n,d,c
  13) Encrypt Given n,e,m
  14) Encrypt Given p,q,e,m
  15) Small N Number Factorization
  16) Common Modulus Attack
  17) Fermat Attack
  18) Wiener Attack
  19) Hastad Attack
  
  99) Exit
  
'''

opt = raw_input('\033[1;34m[=]\033[0m Option: ')

if opt == '99':

    exit()
    
elif opt == '1':

    bits = raw_input('\033[1;34m[=]\033[0m Key Bits: ')
    if bits == '512' or bits == '1024' or bits == '2048' or bits == '4096':
    
        keys = genKeys(bits)
        print(keys[0])
        print('\n')
        print(keys[1])
    
    else:
    
        print('\033[1;31m[-]\033[0m Key Bits must be 512, 1024, 2048 or 4096')
        exit()
    
        

elif opt == '2':

    msgpath = raw_input('\033[1;34m[=]\033[0m Message path: ')
    pubkeypath = raw_input('\033[1;34m[=]\033[0m Public Key path: ')
    etype = raw_input('\033[1;34m[=]\033[0m Output encoding: ')
    ctpth = raw_input('\033[1;34m[=]\033[0m Cipher-Text Outpath: ')
    
    msg = open(msgpath, 'r').read()
    pubk = open(pubkeypath, 'r').read()
    
    ct = encryptRSA(msg, pubk, etype)
    f = open(ctpth, 'w')
    f.write(ct)
    f.close()
    print('\033[1;32m[+]\033[0m Message encrypted successfully')

elif opt == '3':

    msgpath = raw_input('\033[1;34m[=]\033[0m Cipher-Text path: ')
    privkeypath = raw_input('\033[1;34m[=]\033[0m Private Key path: ')
    etype = raw_input('\033[1;34m[=]\033[0m Input encoding: ')
    ctpth = raw_input('\033[1;34m[=]\033[0m Clear-Text Outpath: ')
    
    msg = open(msgpath, 'r').read()
    privk = open(privkeypath, 'r').read()
    
    ct = decryptRSA(msg, privk, etype)
    f = open(ctpth, 'w')
    f.write(ct)
    f.close()
    print('\033[1;32m[+]\033[0m Message decrypted successfully')

elif opt == '4':

    msgpath = raw_input('\033[1;34m[=]\033[0m Message path: ')
    privkeypath = raw_input('\033[1;34m[=]\033[0m Private Key path: ')
    ctpth = raw_input('\033[1;34m[=]\033[0m Signature Outpath: ')
    
    print '''
    
    Options
    --------
      Select a hash for the signature:
      
       1) SHA-512
       2) SHA-384
       3) SHA-256
       4) SHA-1
       5) MD5
       
       '''
    hashn = raw_input('\033[1;34m[=]\033[0m Option: ')
    
    if hashn == '1':
    
        h = 'SHA-512'
    
    elif hashn == '2':
    
        h = 'SHA-384'
    
    elif hashn == '3':
    
        h = 'SHA-256'
    
    elif hashn == '4':
    
        h = 'SHA-1'
    
    elif hashn == '5':
    
        h = 'MD5'
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown option')
        exit()
    
    msg = open(msgpath, 'r').read()
    privk = open(privkeypath, 'r').read()
    
    ct = signRSA(msg, privk, h)
    f = open(ctpth, 'w')
    f.write(ct)
    f.close()
    print('\033[1;32m[+]\033[0m Message signed successfully')

elif opt == '5':

    msgpath = raw_input('\033[1;34m[=]\033[0m Message path: ')
    pubkeypath = raw_input('\033[1;34m[=]\033[0m Public Key path: ')
    signpath = raw_input('\033[1;34m[=]\033[0m Signature Path: ')
    ctpth = raw_input('\033[1;34m[=]\033[0m Verify Outpath: ')
    
    print '''
    
    Options
    --------
      Select a hash for the signature:
      
       1) SHA-512
       2) SHA-384
       3) SHA-256
       4) SHA-1
       5) MD5
       
       '''
    hashn = raw_input('\033[1;34m[=]\033[0m Option: ')
    
    if hashn == '1':
    
        h = 'SHA-512'
    
    elif hashn == '2':
    
        h = 'SHA-384'
    
    elif hashn == '3':
    
        h = 'SHA-256'
    
    elif hashn == '4':
    
        h = 'SHA-1'
    
    elif hashn == '5':
    
        h = 'MD5'
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown option')
        exit()
    
    msg = open(msgpath, 'r').read()
    pubk = open(pubkeypath, 'r').read()
    sign = open(signpath, 'r').read()
    
    ct = verifyRSA(msg, sign, pubk)
    f = open(ctpth, 'w')
    f.write(ct)
    f.close()
    print('\033[1;32m[+]\033[0m Message verified successfully')

elif opt == '6':

    pubpath = raw_input('\033[1;34m[=]\033[0m Public Key path: ')
    pubk = open(pubpath, 'r').read()
    
    extractPub(pubk)

elif opt == '7':

    privpath = raw_input('\033[1;34m[=]\033[0m Private Key path: ')
    privk = open(privpath, 'r').read()
    
    extractPriv(privk)

elif opt == '8':

    n = raw_input('\033[1;34m[=]\033[0m N Number: ')
    e = raw_input('\033[1;34m[=]\033[0m E Number: ')
    out = raw_input('\033[1;34m[=]\033[0m Public Key Outpath: ')
    
    k = embedPub(n,e)
    
    f = open(out, 'w')
    f.write(k)
    f.close()

elif opt == '9':

    p = raw_input('\033[1;34m[=]\033[0m P Number: ')
    q = raw_input('\033[1;34m[=]\033[0m Q Number: ')
    e = raw_input('\033[1;34m[=]\033[0m E Number: ')
    out = raw_input('\033[1;34m[=]\033[0m Private Key Outpath: ')
    
    k = embedPriv(p,q,e)
    
    f = open(out, 'w')
    f.write(k)
    f.close()

elif opt == '10':

    bits = raw_input('\033[1;34m[=]\033[0m Key Bits: ')
    msg = raw_input('\033[1;34m[=]\033[0m Message: ')
    
    if bits == '512' or bits == '1024' or bits == '2048' or bits == '4096':

        m = bytes_to_long(msg)
        genOps(m, bits)
    
    else:
    
        print('\033[1;31m[-]\033[0m Key Bits must be 512, 1024, 2048 or 4096')
        exit()
    
    

elif opt == '11':

    p = raw_input('\033[1;34m[=]\033[0m P Number: ')
    q = raw_input('\033[1;34m[=]\033[0m Q Number: ')
    e = raw_input('\033[1;34m[=]\033[0m E Number: ')
    c = raw_input('\033[1;34m[=]\033[0m C Number: ')
    
    m = RSAsolverpqec(p,q,e,c)
    
    print('\033[1;32m[+]\033[0m Decrypted! m = ' + str(m))
    print('\033[1;34m[*]\033[0m Decoding m...')
    print('\033[1;32m[+]\033[0m ASCII Output: ' + long_to_bytes(m))

elif opt == '12':

    n = raw_input('\033[1;34m[=]\033[0m N Number: ')
    d = raw_input('\033[1;34m[=]\033[0m D Number: ')
    c = raw_input('\033[1;34m[=]\033[0m C Number: ')
    
    m = RSAsolverndc(n,d,c)
    
    print('\033[1;32m[+]\033[0m Decrypted! m = ' + str(m))
    print('\033[1;34m[*]\033[0m Decoding m...')
    print('\033[1;32m[+]\033[0m ASCII Output: ' + long_to_bytes(m))

elif opt == '13':

    n = raw_input('\033[1;34m[=]\033[0m N Number: ')
    e = raw_input('\033[1;34m[=]\033[0m E Number: ')
    m = raw_input('\033[1;34m[=]\033[0m M Number: ')
    
    c = nemEncrypt(n,e,m)
    
    print('\033[1;32m[+]\033[0m Encrypted! c = ' + str(c))

elif opt == '14':

    n = raw_input('\033[1;34m[=]\033[0m P Number: ')
    p = raw_input('\033[1;34m[=]\033[0m Q Number: ')
    e = raw_input('\033[1;34m[=]\033[0m E Number: ')
    m = raw_input('\033[1;34m[=]\033[0m M Number: ')
    
    c = pqemEncrypt(p,q,e,m)
    
    print('\033[1;32m[+]\033[0m Encrypted! c = ' + str(c))

elif opt == '15':

    n = raw_input('\033[1;34m[=]\033[0m N Number: ')
    out = prime_factorize(n)
    print('\033[1;32m[+]\033[0m Factorized! Result: ')
    print(out)

elif opt == '16':

    n = raw_input('\033[1;34m[=]\033[0m N Number: ')
    e1 = raw_input('\033[1;34m[=]\033[0m E1 Number: ')
    e2 = raw_input('\033[1;34m[=]\033[0m E2 Number: ')
    c1 = raw_input('\033[1;34m[=]\033[0m C1 Number: ')
    c2 = raw_input('\033[1;34m[=]\033[0m C2 Number: ')
    
    commonModulus(n,e1,e2,c1,c2)

elif opt == '17':

    n = raw_input('\033[1;34m[=]\033[0m N Number: ')
    e = raw_input('\033[1;34m[=]\033[0m E Number: ')
    
    d = fermatAttack(n,e)
    
    print('\033[1;32m[+]\033[0m Exploited! d = ' + str(d))

elif opt == '18':

    n = raw_input('\033[1;34m[=]\033[0m N Number: ')
    e = raw_input('\033[1;34m[=]\033[0m E Number: ')
    
    d = wienerAttack(n,e)
    
    print('\033[1;32m[+]\033[0m Exploited! d = ' + str(d))

elif opt == '19':

    n0 = raw_input('\033[1;34m[=]\033[0m N0 Number: ')
    n1 = raw_input('\033[1;34m[=]\033[0m N1 Number: ')
    n2 = raw_input('\033[1;34m[=]\033[0m N2 Number: ')
    e = raw_input('\033[1;34m[=]\033[0m E Number: ')
    c0 = raw_input('\033[1;34m[=]\033[0m C0 Number: ')
    c1 = raw_input('\033[1;34m[=]\033[0m C1 Number: ')
    c2 = raw_input('\033[1;34m[=]\033[0m C2 Number: ')
    hastadAttack(n0, n1, n2, e, c0, c1, c2)

else:

    print('\033[1;31m[-]\033[0m Unknown option')
    exit()
