from passlib.hash import des_crypt

def hash(a):

    h = des_crypt.hash(a)
    
    return h
