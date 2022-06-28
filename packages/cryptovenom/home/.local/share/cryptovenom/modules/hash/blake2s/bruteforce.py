import pyblake2

def bf(h, dictionary):

    f = open(dictionary, 'r')
    lines = f.readlines()
    lines = lines.replace('\n', '')
    print('\033[1;34m[*]\033[0m Starting Brute Force - hash = ' + h)
    for i in lines:
    
        m = pyblake2.blake2s()
        m.update(i)
        h2 = m.hexdigest()
    
        if h == h2:
    
            print('\033[1;32m[+]\033[0m Hash Cracked! - Password = ' + i)
            exit()
    print('\033[1;31m[-]\033[0m Hash could not be cracked!')
