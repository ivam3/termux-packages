from passlib.hash import ldap_salted_sha1

def hash(a):

    h = ldap_salted_sha1.hash(a)
    
    return h
