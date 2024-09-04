from passlib.hash import argon2

def hash(a):

    h = argon2.hash(a)
    
    return h
