from passlib.hash import bigcrypt

def hash(a):

    h = bigcrypt.hash(a)
    
    return h
