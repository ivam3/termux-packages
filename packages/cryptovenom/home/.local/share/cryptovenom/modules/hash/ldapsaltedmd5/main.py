from passlib.hash import ldap_salted_md5

def hash(a):

    h = ldap_salted_md5.hash(a)
    
    return h
