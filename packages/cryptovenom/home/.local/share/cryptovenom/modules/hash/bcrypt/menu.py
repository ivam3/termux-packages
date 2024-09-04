from main import *
from bruteforce import *

print '''

-=[OPTIONS]=-

   1) Hash Encrypt
   
   2) Hash Brute Force
   
   '''
   
opt = raw_input('\033[1;34m[=]\033[0m Option: ')


hash1 = raw_input('\033[1;34m[=]\033[0m Hash/Text: ')

saltx = raw_input('\033[1;34m[=]\033[0m [C]ustom or [R]andom Salt: ')

if saltx == 'R' or saltx == 'r':


    saltt = 'gen'
    
    salt = ''


elif saltx == 'c' or saltx == 'C':

    saltt = 'custom'
    
    salt = raw_input('\033[1;34m[=]\033[0m Salt: ')

else:

    print('\033[1;31m[-]\033[0m Unknown option')


f0rmat = raw_input('\033[1;34m[=]\033[0m Output format (Eg.: hex): ')

if opt == '1':

    h = bcryptc(f0rmat, 'print', 'raw', hash1, '', '', saltt, salt)
    print('\033[1;32m[+]\033[0m h(x) = ' + h)

elif opt == '2':

    dic = raw_input('\033[1;34m[=]\033[0m Dictionary path: ')

    bf(hash1, dic)

else:

    print('\033[1;31m[-]\033[0m Unknown option')
