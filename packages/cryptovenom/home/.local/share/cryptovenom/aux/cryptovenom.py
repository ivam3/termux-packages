#!/usr/bin/python

#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
#                    [====={ CRYPTO VENOM }=====]
#
#    | WELCOME TO THE /** CRYPTOVENOM FRAMEWORK **/ |
#
#              ( https://github.com/lockedbyte/cryptovenom )
#
#           << GNU PUBLIC LICENSE >>
#
#                               -/ CREATED BY LOCKEDBYTE /-
#
#                 - [ CONTACT => alejandro.guerrero.rodriguez2@gmail.com ] -
#                 - [ CONTACT => @LockedByte (Twitter) ] -
#
#
# AND NOW...HERE THE CODE
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#

import os
import time
import random
import base64
import commands

# HARDCODED CONFIG

CONFIG_FILEPATH = 'aux/config.conf'
DEBUG_MODE = False
VERSION = '1.0.1'


def banner(version):

    banner1 = '''
  ____                  _     __     __                         
 / ___|_ __ _   _ _ __ | |_ __\ \   / /__ _ __   ___  _ __ ___  
| |   | '__| | | | '_ \| __/ _ \ \ / / _ \ '_ \ / _ \| '_ ` _ \ 
| |___| |  | |_| | |_) | || (_) \ V /  __/ | | | (_) | | | | | |
 \____|_|   \__, | .__/ \__\___/ \_/ \___|_| |_|\___/|_| |_| |_|
            |___/|_|                                            
            
Version: <VERSION>       << The Cryptography Swiss Army knife >>
-------------------------------------------------------------------
'''

    banner2 = ''' 

 _____________
< CryptoVenom >
 -------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\ \n                ||----w |
                ||     ||

Version: <VERSION>       << The Cryptography Swiss Army knife >>
------------------------------------------------------------------
'''

    banner3 = ''' 

    __  ____   __ __  ____  ______   ___   __ __    ___  ____    ___   ___ ___ 
   /  ]|    \ |  |  ||    \|      | /   \ |  |  |  /  _]|    \  /   \ |   |   |
  /  / |  D  )|  |  ||  o  )      ||     ||  |  | /  [_ |  _  ||     || _   _ |
 /  /  |    / |  ~  ||   _/|_|  |_||  O  ||  |  ||    _]|  |  ||  O  ||  \_/  |
/   \_ |    \ |___, ||  |    |  |  |     ||  :  ||   [_ |  |  ||     ||   |   |
\     ||  .  \|     ||  |    |  |  |     | \   / |     ||  |  ||     ||   |   |
 \____||__|\_||____/ |__|    |__|   \___/   \_/  |_____||__|__| \___/ |___|___|
                                                                                
Version: <VERSION>               << The Cryptography Swiss Army knife >>
------------------------------------------------------------------------------
'''

    banner4 = ''' 
                                                                    
   (                         )                                      
   )\   (    (            ( /(      (   (    (                 )    
 (((_)  )(   )\ )  `  )   )\()) (   )\  )\  ))\  (      (     (     
 )\___ (()\ (()/(  /(/(  (_))/  )\ ((_)((_)/((_) )\ )   )\    )\  ' 
((/ __| ((_) )(_))((_)_\ | |_  ((_)\ \ / /(_))  _(_/(  ((_) _((_))  
 | (__ | '_|| || || '_ \)|  _|/ _ \ \ V / / -_)| ' \))/ _ \| '  \() 
  \___||_|   \_, || .__/  \__|\___/  \_/  \___||_||_| \___/|_|_|_|  
             |__/ |_|                                               

Version: <VERSION>      << The Cryptography Swiss Army knife >>
-------------------------------------------------------------------------
'''


    banner5 = ''' 
                                                   
 _____             _       _____                   
|     |___ _ _ ___| |_ ___|  |  |___ ___ ___ _____ 
|   --|  _| | | . |  _| . |  |  | -_|   | . |     |
|_____|_| |_  |  _|_| |___|\___/|___|_|_|___|_|_|_|
          |___|_|                                  

Version: <VERSION>     << The Cryptography Swiss Army knife >>
------------------------------------------------------------------
'''

    banner6 = '\n' + base64.b64decode('IOKWhOKWhMK3IOKWhOKWhOKWhCAgIOKWhMK3IOKWhOKWjCDiloTiloTiloTCt+KWhOKWhOKWhOKWhOKWhCAgICAgICDilowg4paQwrfiloTiloTiloQgLiDilpAg4paEICAgICAgIOKAoiDilowg4paEIMK3LiAK4paQ4paIIOKWjOKWquKWgOKWhCDilojCt+KWkOKWiOKWquKWiOKWiOKWjOKWkOKWiCDiloTilojigKLilojiloggIOKWqiAgICAg4paq4paIwrfilojiloziloDiloQu4paAwrfigKLilojilozilpDilojilqogICAgIMK34paI4paIIOKWkOKWiOKWiOKWiOKWqgrilojilogg4paE4paE4paQ4paA4paA4paEIOKWkOKWiOKWjOKWkOKWiOKWqiDilojilojiloDCtyDilpDilogu4paqIOKWhOKWiOKWgOKWhCDilpDilojilpDilojigKLilpDiloDiloDilqriloTilpDilojilpDilpDilowg4paE4paI4paA4paEIOKWkOKWiCDilozilpDilozilpDilojCtwrilpDilojilojilojilozilpDilojigKLilojilowg4paQ4paI4paAwrcu4paQ4paI4paqwrfigKIg4paQ4paI4paMwrfilpDilojilowu4paQ4paMIOKWiOKWiOKWiCDilpDilojiloTiloTilozilojilojilpDilojilozilpDilojilowu4paQ4paM4paI4paIIOKWiOKWiOKWjOKWkOKWiOKWjArCt+KWgOKWgOKWgCAu4paAICDiloAgIOKWgCDigKIgLuKWgCAgICDiloDiloDiloAgIOKWgOKWiOKWhOKWgOKWqi4g4paAICAg4paA4paA4paAIOKWgOKWgCDilojilqog4paA4paI4paE4paA4paq4paA4paAICDilojilqriloDiloDiloAK') +'''
Version: <VERSION>        << The Cryptography Swiss Army knife >>
--------------------------------------------------------------------'''
 
    try:
        banners = [banner1, banner2, banner3, banner4, banner5, banner6, banner6, banner6, banner6]
        random_number = random.randint(0, len(banners))
    
        print(banners[random_number].replace('<VERSION>', version))
        
    except:
    
        print(banner1.replace('<VERSION>', version))
    

def menu(menu):

    if menu == 'main':
    
        print('''-[MENU]-
        
    0) Crackssistant (NOT YET)
    1) Symmetric Algorithms
    2) Asymmetric Algorithms
    3) Encoding Algorithms
    4) Classical Algorithms
    5) Hash Algorithms
    6) Mathematical Functions
    7) Algorithm Identifiers (Not YET)
    8) String Manipulation
    9) Randomization Functions
   10) Other
   11) About CryptoVenom
    
   99) Exit
   
''')
        option = raw_input('\033[1;34m[=]\033[0m Option: ')
        
        if option == '99':
        
            print('\033[1;34m[*]\033[0m Exiting...')
            exit()
            
        elif option == '0':
        
            return 'crackssistant'
            
        elif option == '1':
        
            return 'symmetric'
        
        elif option == '2':
        
            return 'asymmetric'
        
        elif option == '3':
        
            return 'encoding'
        
        elif option == '4':
        
            return 'classical'
            
        elif option == '5':
        
            return 'hash'
            
        elif option == '6':
        
            return 'math'
            
        elif option == '7':
        
            return 'identifiers'
            
        elif option == '8':
        
            return 'string'
            
        elif option == '9':
        
            return 'random'
            
        elif option == '10':
        
            return 'other'
            
        elif option == '11':
        
            return 'about'
        
        else:
        
            print('\033[1;31m[-]\033[0m Unknown option')

    elif menu == 'crackssistant':
    
        print('''
-[MENU]-

[%]...STILL IN DEVELOPMENT...[%]
    
    
''')
    
    elif menu == 'symmetric':
    
        print('''
-[MENU:Symmetric]-

    1) AES / Rijndael (Advanced Encryption Algorithm)
    2) DES (Data Encryption Standard)
    3) XOR Cipher
    4) Blowfish
    5) Twofish
    6) 3DES / TDES (Triple DES)
    7) RC2 (Ron's Code 2)
    8) RC4 (Ron's Code 4)
    9) CAST
   10) SCrypt
   
   99) Exit
    
    
''')

        option = raw_input('\033[1;34m[=]\033[0m Option: ')
        
        if option == '99':
    
            print('\033[1;34m[*]\033[0m Exiting')
            exit()
    
        elif option == '1':
    
            os.system('python modules/symetric/aes/menu.py auto')
    
        elif option == '2':
    
            os.system('python modules/symetric/des/menu.py auto')
    
        elif option == '3':
    
            os.system('python modules/symetric/xor/menu.py auto')
    
        elif option == '4':
    
            os.system('python modules/symetric/blowfish/menu.py auto')
    
        elif option == '5':
     
            os.system('python modules/symetric/twofish/menu.py auto')
    
        elif option == '6':
    
            os.system('python modules/symetric/3des/menu.py auto')
    
        elif option == '7':
    
            os.system('python modules/symetric/rc2/menu.py auto')
    
        elif option == '8':
    
            os.system('python modules/symetric/rc4/menu.py auto')
    
        elif option == '9':
    
            os.system('python modules/symetric/cast/menu.py auto')
            
        elif option == '10':
    
            os.system('python modules/symetric/scrypt/menu.py auto')
    
        else:
    
            print('\033[1;31m[-]\033[0m Unknown option')
    
    elif menu == 'asymmetric':
    
        print('''
-[MENU:Asymmetric]-

    1) RSA
    2) Diffie-Hellman (DH)
    3) DSA (Digital Signature Algorithm)
    
   99) Exit
    
    
''')

        option = raw_input('\033[1;34m[=]\033[0m Option: ')
    
        if option == '99':
    
            print('\033[1;34m[*]\033[0m Exiting')
            exit()
    
        elif option == '1':
    
            os.system('python modules/asymetric/rsa/menu.py auto')
    
        elif option == '2':
    
            os.system('python modules/asymetric/diffiehellman/menu.py auto')
    
        elif option == '3':
    
            os.system('python modules/asymetric/dsa/menu.py auto')

    
        else:
    
            print('\033[1;31m[-]\033[0m Unknown option')

    elif menu == 'encoding':
    
        print('''
-[MENU:Encoding]-

    1) Base64
    2) Base32
    3) Base16
    4) Base58
    5) Base85
    6) Base91
    7) Hexadecimal
    8) Binary
    9) Octal
   10) Decimal
   11) URL
   12) ROT-x
   
   99) Exit

    
''')

        option = raw_input('\033[1;34m[=]\033[0m Option: ')
    
        if option == '99':
    
            print('\033[1;34m[*]\033[0m Exiting')
            exit()
    
        elif option == '1':
    
            os.system('python modules/encoding/base64/menu.py auto')
    
        elif option == '2':
    
            os.system('python modules/encoding/base32/menu.py auto')
     
        elif option == '3':
    
            os.system('python modules/encoding/base16/menu.py auto')
    
        elif option == '4':
    
            os.system('python modules/encoding/base58/menu.py auto')
    
        elif option == '5':
    
            os.system('python modules/encoding/base85/menu.py auto')
            
        elif option == '6':
    
            os.system('python modules/encoding/base91/menu.py auto')
    
        elif option == '7':
    
            os.system('python modules/encoding/hexadecimal/menu.py auto')
    
        elif option == '8':
    
            os.system('python modules/encoding/binary/menu.py auto')
    
        elif option == '9':
    
            os.system('python modules/encoding/octal/menu.py auto')
    
        elif option == '10':
    
            os.system('python modules/encoding/decimal/menu.py auto')
    
        elif option == '11':
    
            os.system('python modules/encoding/url/menu.py auto')
    
        elif option == '12':
    
            os.system('python modules/encoding/rot/menu.py auto')
              
        else:
    
            print('\033[1;31m[-]\033[0m Unknown option')
        
    elif menu == 'classical':
    
        print('''
-[MENU:Classical]-

    1) Caesar
    2) Vigenere Cipher
    3) Playfair Cipher
    4) Polybius Square
    5) Morse
    6) Atbash
    7) Baconian
    8) AutoKey
    9) Beaufort Cipher
   10) Railfence Cipher
   11) Simple Substitution Cipher
   12) Columnar Tramposition
   13) Bifid
   14) Foursquare Cipher
   15) Fractionated Morse
   16) Enigma
   17) Gronsfeld Cipher
   18) Porta
   19) RunningKey
   20) ADFGVX Cipher
   21) ADFGX Cipher
   22) Affine Cipher
   23) Vernam Cipher

   99) Exit
    
''')   

        option = raw_input('\033[1;34m[=]\033[0m Option: ')
    
        if option == '99':
    
            print('\033[1;34m[*]\033[0m Exiting')
            exit()
    
        elif option == '1':
    
            os.system('python modules/classical/caesar/menu.py auto')
    
        elif option == '2':
    
            os.system('python modules/classical/vigenere/menu.py auto')
    
        elif option == '3':
    
            os.system('python modules/classical/playfair/menu.py auto')
    
        elif option == '4':
    
            os.system('python modules/classical/polybius/menu.py auto')
    
        elif option == '5':
    
            os.system('python modules/classical/morse/menu.py auto')
    
        elif option == '6':
    
            os.system('python modules/classical/atbash/menu.py auto')
    
        elif option == '7':
    
            os.system('python modules/classical/baconian/menu.py auto')
    
        elif option == '8':
    
            os.system('python modules/classical/autokey/menu.py auto')
    
        elif option == '9':
    
            os.system('python modules/classical/beaufort/menu.py auto')
    
        elif option == '10':
    
            os.system('python modules/classical/railfence/menu.py auto')
      
        elif option == '11':
     
            os.system('python modules/classical/substitution/menu.py auto')
        
        elif option == '12':
    
            os.system('python modules/classical/coltrans/menu.py auto')
    
        elif option == '13':
    
            os.system('python modules/classical/bifid/menu.py auto')
    
        elif option == '14':
    
            os.system('python modules/classical/foursquare/menu.py auto')
      
        elif option == '15':
    
           os.system('python modules/classical/fractionatedmorse/menu.py auto')
    
        elif option == '16':
    
            os.system('python modules/classical/enigma/menu.py auto')
    
        elif option == '17':
    
            os.system('python modules/classical/gronsfeld/menu.py auto')
    
        elif option == '18':
    
            os.system('python modules/classical/porta/menu.py auto')
    
        elif option == '19':
    
            os.system('python modules/classical/runningkey/menu.py auto')

        elif option == '20':
    
            os.system('python modules/classical/adfgvx/menu.py auto')
            
        elif option == '21':
    
            os.system('python modules/classical/adfgx/menu.py auto')

        elif option == '22':
    
            os.system('python modules/classical/affine/menu.py auto')

        elif option == '23':
    
            os.system('python modules/classical/vernam/menu.py auto')
        
        else:
    
            print('\033[1;31m[-]\033[0m Unknown option')
        
    elif menu == 'hash':
    
        print('''
-[MENU:Hashing]-

    1) MD5
    2) SHA-1
    3) SHA-224
    4) SHA-256
    5) SHA-384
    6) SHA-512
    7) MD2
    8) MD4
    9) Argon2
   10) BCrypt
   11) BigCrypt Unix
   12) Blake2b
   13) Blake2s
   14) BSDi Crypt Unix
   15) Cisco ASA Hash
   16) Cisco PIX Hash
   17) Cisco Type 7
   18) Crypt-16 Unix
   19) DES Crypt Unix
   20) FreeBSD Unix
   21) HMAC
   22) LDAP-MD5
   23) LDAP Salted MD5
   24) LDAP SHA-1
   25) LDAP Salted SHA-1
   26) LMHash
   27) MD5 Unix
   28) MSDCC Hash
   29) MSDCC 2 Hash
   30) MSSQL 2000 Hash
   31) MSSQL 2005 Hash
   32) MySQL 41 Hash
   33) MySQL 323 Hash
   34) NTHash
   35) NTLM Hash
   36) Oracle 10 Hash
   37) Oracle 11 Hash
   38) PHPass Hash
   39) PostgreSQL MD5
   34) RIPEMD
   41) SCrypt
   42) SHA-256 Unix
   43) SHA-512 Unix
   44) Sun MD5 Unix

   99) Exit
    
''')   

        option = raw_input('\033[1;34m[=]\033[0m Option: ')
    
        if option == '99':
    
            print('\033[1;34m[*]\033[0m Exiting')
            exit()
    
        elif option == '1':
    
            os.system('python modules/hash/md5/menu.py auto')
    
        elif option == '2':
    
            os.system('python modules/hash/sha1/menu.py auto')
    
        elif option == '3':
    
            os.system('python modules/hash/sha224/menu.py auto')
    
        elif option == '4':
    
            os.system('python modules/hash/sha256/menu.py auto')
    
        elif option == '5':
    
            os.system('python modules/hash/sha384/menu.py auto')
    
        elif option == '6':
    
            os.system('python modules/hash/sha512/menu.py auto')
    
        elif option == '7':
    
            os.system('python modules/hash/md2/menu.py auto')
     
        elif option == '8':
    
            os.system('python modules/hash/md4/menu.py auto')
    
        elif option == '9':
    
            os.system('python modules/hash/argon2/menu.py auto')
    
        elif option == '10':
    
            os.system('python modules/hash/bcrypt/menu.py auto')
    
        elif option == '11':
    
            os.system('python modules/hash/bigcryptunix/menu.py auto')
    
        elif option == '12':
    
            os.system('python modules/hash/blake2b/menu.py auto')
        
        elif option == '13':
    
            os.system('python modules/hash/blake2s/menu.py auto')
    
        elif option == '14':
    
            os.system('python modules/hash/bsdicryptunix/menu.py auto')
    
        elif option == '15':
    
            os.system('python modules/hash/ciscoasa/menu.py auto')
    
        elif option == '16':
    
            os.system('python modules/hash/ciscopix/menu.py auto')    

        elif option == '17':
    
            os.system('python modules/hash/ciscotype7/menu.py auto')
    
        elif option == '18':
    
            os.system('python modules/hash/crypt16unix/menu.py auto')
    
        elif option == '19':
    
            os.system('python modules/hash/descryptunix/menu.py auto')
     
        elif option == '20':
    
            os.system('python modules/hash/freebsdunix/menu.py auto')
    
        elif option == '21':
    
            os.system('python modules/hash/hmac/menu.py auto')
    
        elif option == '22':
    
            os.system('python modules/hash/ldapmd5/menu.py auto')
    
        elif option == '23':
    
            os.system('python modules/hash/ldapsaltedmd5/menu.py auto')
    
        elif option == '24':
    
            os.system('python modules/hash/ldapsha1/menu.py auto')
        
        elif option == '25':
    
            os.system('python modules/hash/ldapsaltedsha1/menu.py auto')
    
        elif option == '26':
    
            os.system('python modules/hash/lmhash/menu.py auto')
    
        elif option == '27':
    
            os.system('python modules/hash/md5unix/menu.py auto')
    
        elif option == '28':
    
            os.system('python modules/hash/msdcc/menu.py auto')    
            
        elif option == '29':
    
            os.system('python modules/hash/msdcc2/menu.py auto')
        
        elif option == '30':
    
            os.system('python modules/hash/mssql2000/menu.py auto')
    
        elif option == '31':
    
            os.system('python modules/hash/mssql2005/menu.py auto')
    
        elif option == '32':
    
            os.system('python modules/hash/mysql41/menu.py auto')
    
        elif option == '33':
    
            os.system('python modules/hash/mysql323/menu.py auto')   
            

        elif option == '34':
    
            os.system('python modules/hash/nthash/menu.py auto')    
            
        elif option == '35':
    
            os.system('python modules/hash/ntlm/menu.py auto')
        
        elif option == '36':
    
            os.system('python modules/hash/oracle10/menu.py auto')
    
        elif option == '37':
    
            os.system('python modules/hash/oracle11/menu.py auto')
    
        elif option == '38':
    
            os.system('python modules/hash/phpass/menu.py auto')
    
        elif option == '39':
    
            os.system('python modules/hash/postgresmd5/menu.py auto')   
            

        elif option == '40':
    
            os.system('python modules/hash/ripemd/menu.py auto')
        
        elif option == '41':
    
            os.system('python modules/hash/scrypt/menu.py auto')
    
        elif option == '42':
    
            os.system('python modules/hash/sha256unix/menu.py auto')
    
        elif option == '43':
    
            os.system('python modules/hash/sha512unix/menu.py auto')
    
        elif option == '44':
    
            os.system('python modules/hash/sunmd5unix/menu.py auto')   
        
        else:
    
            print('\033[1;31m[-]\033[0m Unknown option')
            
    elif menu == 'math':
    
        print('''
-[MENU:Mathematical]-

    1) Extended Ecluidean Algorithm
    2) Fast Exponentiation Algorithm
    3) Factorize product of primes

   99) Exit
    
''')   

        option = raw_input('\033[1;34m[=]\033[0m Option: ')
    
        if option == '99':
    
            print('\033[1;34m[*]\033[0m Exiting')
            exit()
    
        elif option == '1':
    
            os.system('python modules/math/exteuc/menu.py auto')
    
        elif option == '2':
    
            os.system('python modules/math/fastexp/menu.py auto')
    
        elif option == '3':
    
            os.system('python modules/math/primefactor/menu.py auto')
        
        else:
    
            print('\033[1;31m[-]\033[0m Unknown option')
            
    elif menu == 'identifiers':
    
        print('''
-[MENU:Identifiers]-

    1) Encoding Identifiers
    2) Hash Identifiers
    3) Language Identifiers

   99) Exit
    
''')   

        option = raw_input('\033[1;34m[=]\033[0m Option: ')
    
        if option == '99':
    
            print('\033[1;34m[*]\033[0m Exiting')
            exit()
    
        elif option == '1':
    
            os.system('python modules/identifiers/encoding/menu.py auto')
    
        elif option == '2':
    
            os.system('python modules/identifiers/hash/menu.py auto')
    
        elif option == '3':
    
            os.system('python modules/identifiers/lang/menu.py auto')
        
        else:
    
            print('\033[1;31m[-]\033[0m Unknown option')

    elif menu == 'string':
    
        print('''
-[MENU:String]-

    1) String to Upper Case
    2) String to Lower Case
    3) Reverse String
    4) Block Reverse String
    5) Remove Spaces
    6) Remove Enters
    7) Invert Case
    8) One-Byte List
    9) Add Line Numbers
   10) String Replacement

   99) Exit
    
''')   

        option = raw_input('\033[1;34m[=]\033[0m Option: ')
    
        if option == '99':
    
            print('\033[1;34m[*]\033[0m Exiting')
            exit()
    
        elif option == '1':
    
            os.system('python modules/string/upper/menu.py auto')
    
        elif option == '2':
    
            os.system('python modules/string/lower/menu.py auto')
    
        elif option == '3':
    
            os.system('python modules/string/reverse/menu.py auto')
    
        elif option == '4':
    
            os.system('python modules/string/blockreverse/menu.py auto')
    
        elif option == '5':
    
            os.system('python modules/string/removespaces/menu.py auto')
    
        elif option == '6':
    
            os.system('python modules/string/removeenters/menu.py auto')
    
        elif option == '7':
    
            os.system('python modules/string/reversecase/menu.py auto')
    
        elif option == '8':
    
            os.system('python modules/string/onebytelist/menu.py auto')
    
        elif option == '9':
    
            os.system('python modules/string/addlinenumbers/menu.py auto')
    
        elif option == '10':
    
            os.system('python modules/string/replace/menu.py auto')
        
        else:
    
            print('\033[1;31m[-]\033[0m Unknown option')       

    elif menu == 'random':
    
        print('''
-[MENU:Randomization]-

    1) Random String
    2) Random Number
    3) Random IV (Initialization Vector)

   99) Exit
    
''')   

        option = raw_input('\033[1;34m[=]\033[0m Option: ')
    
        if option == '99':
    
            print('\033[1;34m[*]\033[0m Exiting')
            exit()
    
        elif option == '1':
    
            os.system('python modules/random/randomstring/menu.py auto')
    
        elif option == '2':
    
            os.system('python modules/random/randomnumber/menu.py auto')
    
        elif option == '3':
    
            os.system('python modules/random/randomiv/menu.py auto')
        
        else:
    
            print('\033[1;31m[-]\033[0m Unknown option')

    elif menu == 'other':
    
        print('''
-[MENU:Other]-

    1) PGP Functions
    2) Logic Operation XOR
    3) Logic Operation XNOR
    4) Logic Operation AND
    5) Logic Operation NAND
    6) Logic Operation OR
    7) Logic Operation NOR
    8) Logic Operation NOT

   99) Exit
    
''')   

        option = raw_input('\033[1;34m[=]\033[0m Option: ')
    
        if option == '99':
    
            print('\033[1;34m[*]\033[0m Exiting')
            exit()
    
        elif option == '1':
    
            os.system('python modules/other/pgp/menu.py auto')
    
        elif option == '2':
    
            os.system('python modules/other/xor/menu.py auto')
    
        elif option == '3':
    
            os.system('python modules/other/xnor/menu.py auto')
    
        elif option == '4':
    
            os.system('python modules/other/and/menu.py auto')
    
        elif option == '5':
    
            os.system('python modules/other/nand/menu.py auto')
    
        elif option == '6':
    
            os.system('python modules/other/or/menu.py auto')
    
        elif option == '7':
    
            os.system('python modules/other/nor/menu.py auto')
    
        elif option == '8':
    
            os.system('python modules/other/not/menu.py auto')    
        
        else:
    
            print('\033[1;31m[-]\033[0m Unknown option')


    elif menu == 'about':
    
        print('''
-[MENU:About CryptoVenom]-

CryptoVenom. The Cryptography Swiss Army Knife

-[ Created By LockedByte ]-

Public Key:

-----BEGIN PGP PUBLIC KEY BLOCK-----

mQGNBF2rm0wBDADQylilJzH2QgFC8Y9vF6IuT4LRVA+HlNkKQGM6hyLusZcbjggX
ZCBX7ls7ghpsiJdUX9LdLOtVX45kAGy0RxjhshGyUF+FOOGyq2q0yQekKfBj8X55
KviLqbpupuadcJP/Jxdsd6r4EhnUOcQZC1Cf0HBYX6Azg6TjDaSV2OKBmSO4dJk5
BhDmrGLzXjJnDbames9Cmvh2JbL43OhwuzeT1zqYpPJIseFXfMS//iYpoAhDN89C
GZE0w96b9ZN6W+54NoF8DoOTJ6W6Z4ZiuOcMIA0itO5qsfkgNH2X7/KZAg8Mtk4a
dfzxsKRXMkR8vddo+IzSLoguXTPLxK5ZDZtHBZIL/LCx5H6YzOBujP523oVb1uig
WrFUHaAOVNFGAKsv7WTvBhCMTVlRh+ulFaXGWK3+w2PSvgWf9maOZkktxnx6V8XW
hboNbg5aUbzrAX7dT0bXSHlusupIjlTn8ml+7rrMem9wadOzC45hOsd0SYm4f8mY
IVrmjx7jeXiMHUUAEQEAAbRGQWxlamFuZHJvIEd1ZXJyZXJvIFJvZHJpZ3VleiA8
YWxlamFuZHJvLmd1ZXJyZXJvLnJvZHJpZ3VlejJAZ21haWwuY29tPokB1AQTAQoA
PhYhBMM+WtjJNFah41yjjSJlVkdktaG8BQJdq5tMAhsDBQkDwmcABQsJCAcCBhUK
CQgLAgQWAgMBAh4BAheAAAoJECJlVkdktaG8OEAL/2ujvxBV9Qso6dLmx/YQm7il
KboA6zLvbWhUeHKJPdaKi3uZxZmDVnDKuQZS0FQTn5MiiBUvU6vlbnpUEbyHz/T2
h/QN+tXUp7zKsdI+REhFhc7IW9J0ZMaCzJWA6aFe8Z1H/+UBTssP5xIbyHirzM/7
rJsb24cxj5y5kzqXHz7i1MhgqkeoKCUtsW3F0yQqpjRmv1GQa4RReD7PONeu6cET
8bSsTYHCeyOD/NnNDo+FSiM+GdTzryJEo1QpFMKH8zq0ZoNUVVZnZYxntSjMQXGt
b0cpaWZ1Tw7uCOX6xEghiGg590XForaVMHvr+rP9Wpx2tbjdswWxTbalwlzup0KS
WovS+CscNrJy1Yiz/rWXOfCJlSEt63O76VVbWqfGOOpnYsa81j3RrvTjSpJ9ux7F
4QQg+Nt+lpjg/MqYvQS8tE3j2wWI6F+ZfnozjKNbR1P0UImEXk/v+4QVoVJfNz6o
WWmQaqWMCtnJeY1N0he+7Jaj0QWl2auEgcng+Tgv1LkBjQRdq5tMAQwAwYHmgD3K
BWUDN2/YJCG2DibDxQ8G0Oc3dMaxEJWFPP8dvY9jkaTrGiLb1TfvFRKOETK7gZDE
FI4GDQYp9M83eF8wLM0jXb0UfCtTv/gcI8AqkCV5pcS86k/0A2VNwtNyWB0ldLR0
zMtS1vn3D3xbQ0HmGncQX0MN9nzHhr7pDsT8v97BiYkyJ06odVPG6vtVDggWgw66
b8kDDVywjUmuqHAMthmauD7pl01oTc23ugdJHpIYYtFRnJDqd3nlFD+97jxC7COw
cKs1+Q5P0fwGYp2nKIrV9K/1rpjPSDYrq7Hpa+uMPi09KQskvmnXlaDe+1MPwzUu
i1jeGSiWDsta2Zy3ScMvQfRjb27SZNyesDbA/R9kCUOTgHA98m9DKFgNiQobwy28
iB7s5bT5ddbXIYqsdCrZiD38+8fgc8OW/+mDjamudOe1PkwnroSlUuIV6kyNrzMK
sme09oCwPNHO9LCtt9mJ9AZ/nu92JDd6k98ofZ8VBOKXOlWqDsv7OzwtABEBAAGJ
AbwEGAEKACYWIQTDPlrYyTRWoeNco40iZVZHZLWhvAUCXaubTAIbDAUJA8JnAAAK
CRAiZVZHZLWhvCGlC/47plWOrl5EHNCjWOYystdDDJcsJHhVsDPSBFuVqq8v8uyD
vTrrMJ6YIkoluYJ9x6mI8oD1aR+zE1XXSIsSrHeqc9uYzVbI1asf5kxi1h6AatpV
VLCTcNwxMFmRlpL9vKaVq+qxrZ38Wanur3wnLVvOHnIufvgPXMFXYXn+A/m0X8hi
YnWkNN219hi/L+MSGcglf8eyZwE142V3Bj6k4APziC7+Pwuhopwpdojq2QJtD+k1
JndUW5OFi/CHxIl7DkmIyEmlCaIFUBJzZ4VkqDrQU1vuTH9DbPHtUbyAQP0Ktuer
wDg2oghtiTO9JEQ+c0roFFjaINFrDSWJsGybETgUOIcb26El0Ngqzf6Kn9CsGDwU
3eyVH+7ykXfLBDC4lt5+yJ0SbQeFflzMnBmVBnlhmz9y3k5nU0A6/pLI5qetg/D4
njiwI/3ldFMPgP01tyZg4e+a8nYvrZVr3cDmiWzyDvI8m0P36NHZ4L0I8Gvl7ARC
OFK4oKrrQy5fIqVo57U=
=WVh5
-----END PGP PUBLIC KEY BLOCK-----



- [ CONTACT => alejandro.guerrero.rodriguez2@gmail.com ] -
- [ CONTACT => @LockedByte (Twitter) ] -

GPG:

        [ C3 3E 5A D8 C9 34 56 A1 E3 5C A3 8D 22 65 56 47 64 B5 A1 BC ]
   
        
''')


    else:

        print('\033[1;31m[-]\033[0m Unknown error.')
        return 'err'

def configSetup(CONFIG_FILEPATH):

    lang = raw_input('\033[1;34m[=]\033[0m Your Lang [Eg.: EN]: ')

    
    print('\033[1;34m[*]\033[0m Saving configuration in: ' + CONFIG_FILEPATH)
    config = 'LANG = ' + lang
    configfile = open(CONFIG_FILEPATH, 'w')
    configfile.write(config)
    configfile.close()
    print('\033[1;32m[+]\033[0m Configuration applied successfully')
    time.sleep(4)
    
def checkConfig(CONFIG_FILEPATH):

    try:

        os.path.isfile(CONFIG_FILEPATH)
        return True
    
    except:

        print('\033[1;33m[!]\033[0m Configuration file does not exists, running configuration setup')
    
        return False
        

check = checkConfig(CONFIG_FILEPATH)

if not check:

    while not check:
    
        configSetup(CONFIG_FILEPATH)
        check = checkConfig(CONFIG_FILEPATH)
        os.system('clear')
        

banner(VERSION)
ret = menu('main')
menu(ret)
    
while True:
    raw_input('\n\n\033[1;34m[*]\033[0m Continue to main? ')
    print('\n\n')
    ret = menu('main')
    menu(ret)

