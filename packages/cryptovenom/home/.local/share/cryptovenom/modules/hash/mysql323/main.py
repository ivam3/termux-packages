from passlib.hash import mysql323

def hash(a):

    h = mysql323.hash(a)
    
    return h
