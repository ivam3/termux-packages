from passlib.hash import cisco_pix

def hash(a):

    h = cisco_pix.hash(a)
    
    return h
