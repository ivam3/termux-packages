from passlib.hash import oracle10

def hash(a):

    h = oracle10.hash(a)
    
    return h
