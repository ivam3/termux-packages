from passlib.hash import lmhash

def hash(a):

    h = lmhash.hash(a)
    
    return h
