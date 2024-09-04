from passlib.hash import phpass

def hash(a):

    h = phpass.hash(a)
    
    return h
