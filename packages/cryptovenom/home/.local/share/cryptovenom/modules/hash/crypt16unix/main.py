from passlib.hash import crypt16

def hash(a):

    h = crypt16.hash(a)
    
    return h
