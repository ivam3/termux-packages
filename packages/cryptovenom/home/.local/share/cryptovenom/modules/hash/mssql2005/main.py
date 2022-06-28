from passlib.hash import mssql2005

def hash(a):

    h = mssql2005.hash(a)
    
    return h
