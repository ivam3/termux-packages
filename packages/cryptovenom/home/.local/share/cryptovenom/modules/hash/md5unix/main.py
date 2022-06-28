from passlib.hash import md5_crypt

def hash(a):

    h = md5_crypt.hash(a)
    
    return h
