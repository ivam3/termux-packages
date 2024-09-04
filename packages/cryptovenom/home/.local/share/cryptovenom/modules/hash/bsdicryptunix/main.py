from passlib.hash import bsdi_crypt

def hash(a):

    h = bsdi_crypt.hash(a)
    
    return h
