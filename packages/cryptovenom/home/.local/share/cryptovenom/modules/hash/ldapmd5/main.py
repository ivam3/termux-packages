from passlib.hash import ldap_md5

def hash(a):

    h = ldap_md5.hash(a)
    
    return h
