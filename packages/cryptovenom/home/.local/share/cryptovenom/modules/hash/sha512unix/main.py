from passlib.hash import sha512_crypt

def hash(a):

    h = sha512_crypt.hash(a)
    
    return h
