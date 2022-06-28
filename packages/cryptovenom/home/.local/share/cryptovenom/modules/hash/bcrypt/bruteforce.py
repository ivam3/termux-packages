import bcrypt

def bf(h, dictionary, salt):

    f = open(dictionary, 'r')
    lines = f.readlines()
    lines = lines.replace('\n', '')
    print('\033[1;34m[*]\033[0m Starting Brute Force - hash = ' + h)
    for i in lines:
    
        h2 = bcrypt.hashpw(i, salt)
    
        if h == h2:
    
            print('\033[1;32m[+]\033[0m Hash Cracked! - Password = ' + i)
            exit()
    print('\033[1;31m[-]\033[0m Hash could not be cracked!')
