from main import *

print '''

-=[OPTIONS]=-

   1) Algorithm Encrypt
   
   '''
   
opt = raw_input('\033[1;34m[=]\033[0m Option: ')


hash1 = raw_input('\033[1;34m[=]\033[0m Hash/Text: ')

if opt == '1':

    h = hash(hash1)
    print('\033[1;32m[+]\033[0m h(x) = ' + h)

else:

    print('\033[1;31m[-]\033[0m Unknown option')
