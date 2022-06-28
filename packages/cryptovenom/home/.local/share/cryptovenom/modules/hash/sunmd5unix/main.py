from passlib.hash import sun_md5_crypt

def hash(a):

    h = sun_md5_crypt.hash(a)
    
    return h
