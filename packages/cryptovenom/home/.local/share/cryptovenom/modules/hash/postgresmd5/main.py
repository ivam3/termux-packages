from passlib.hash import postgres_md5

def hash(a, user):

    h = postgres_md5.hash(a, user)
    
    return h
