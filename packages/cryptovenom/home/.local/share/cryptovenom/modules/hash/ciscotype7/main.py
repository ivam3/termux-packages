from passlib.hash import cisco_type7

def hash(a):

    h = cisco_type7.hash(a)
    
    return h
