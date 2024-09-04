from passlib.hash import mssql2000

def hash(a):

    h = mssql2000.hash(a)
    
    return h
