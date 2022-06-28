from passlib.hash import sha256_crypt

def hash(a):

    h = sha256_crypt.hash(a)
    
    return h
