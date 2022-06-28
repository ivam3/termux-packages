from passlib.hash import mysql41

def hash(a):

    h = mysql41.hash(a)
    
    return h
