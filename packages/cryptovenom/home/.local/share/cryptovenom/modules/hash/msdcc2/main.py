from passlib.hash import msdcc2

def hash(a, user1):

    h = msdcc2.hash(a, user1)
    
    return h
