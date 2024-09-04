from passlib.hash import msdcc

def hash(a, user1):

    h = msdcc.hash(a, user1)
    
    return h
