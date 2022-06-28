from passlib.hash import ldap_sha1

def hash(a):

    h = ldap_sha1.hash(a)
    
    return h
