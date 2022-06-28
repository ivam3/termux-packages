from passlib.hash import oracle11

def hash(a):

    h = oracle11.hash(a)
    
    return h
