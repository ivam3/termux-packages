from passlib.hash import nthash

def hash(a):

    h = nthash.hash(a)
    
    return h
