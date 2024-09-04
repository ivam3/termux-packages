from passlib.hash import bsd_nthash

def hash(a):

    h = bsd_nthash.hash(a)
    
    return h
