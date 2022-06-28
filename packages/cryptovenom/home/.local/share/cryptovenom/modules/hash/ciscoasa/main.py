from passlib.hash import cisco_asa

def hash(a):

    h = cisco_asa.hash(a)
    
    return h
