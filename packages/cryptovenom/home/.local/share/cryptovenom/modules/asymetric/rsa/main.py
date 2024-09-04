#!/usr/bin/python

#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
#                    [====={ CRYPTO VENOM }=====]
#
#     | ATTENTION!: THIS SOFTWARE IS PART OF THE "CRYPTOVENOM FRAMEWORK" |
#
#              ( https://github.com/lockedbyte/cryptovenom )
#
#           << GNU PUBLIC LICENSE >>
#
#                               / CREATED BY LOCKEDBYTE /
#
#                  [ CONTACT => alejandro.guerrero.rodriguez2@gmail.com ]
#                  [ CONTACT => @LockedByte (Twitter) ]
#
#
# AND NOW...HERE THE CODE
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import *
from Crypto import Random
import zlib
import base64
import Crypto
from random import randint
import argparse
import ast
import random
import gmpy2
import codecs
import math
from sys import setrecursionlimit
import fractions
from Crypto.Util.number import *

def inverse(n1,n2):
    try:
        n3 = gmpy2.invert(n1,n2)
    except ZeroDivisionError:
        n3 = 'ERR'
    return n3
def bits_of(m):
    n=int(m)
    while n:
        yield n & 1
        n >>= 1
 
def fast_exp(x,n):
    result = 1
    partial = x
 
    for bit in bits_of(n):
        if bit:
            result *= partial
        partial ^= 2
 
    return result
    
class Hastad(object):


  sys.setrecursionlimit(1000000)

  def xgcd(self, a, b):
    if a == 0:
      return (b, 0, 1)
    else:
      gcd, u, v = self.xgcd(b % a, a)
      return (gcd, v - (b // a) * u, u)

  def root(self, a, e):
  	return (gmpy2.iroot(a,e))
    

class Comod(object):

    setrecursionlimit(1000000)

    def xgcd(self, a, b):
      if a == 0:
        return (b, 0, 1)
      else:
        gcd, u, v = self.xgcd(b % a, a)
        return (gcd, v - (b // a) * u, u)

    def modinv(self, a, n):
      g, x, y = self.xgcd(a, n)
      return x % n

    def pow_mod(self, a, b, n):
      number = 1
      while b:
        if b & 1:
          number = number * a % n
        b >>= 1
        a = a * a % n
      return number
        
class Fermat(object):

    def carre_parfait(self, x):

      if x < 1:

        return(False)

      sqrt_x = math.sqrt(x)

      return (sqrt_x == int(math.floor(sqrt_x)))

    def fermat(self,n):

      a = 2*math.ceil(math.sqrt(n)) + 1

      aux = 2 * a +1

      n4 = 4 * n

      c = pow(a, 2) - n4

      while not carre_parfait(c):

        c += aux

        a += 1

        aux += 2

      b = int(math.sqrt(c))

      p = (a - b) // 2

      q = (a + b) // 2

      if (p*q != n):

        print("Error!")
        exit(0)

      return (p, q)

    def indicatrice_euler(self, p, q):

      return((p - 1) * (q - 1))

    def bezout(self, a, b):

        if a == 0 and b == 0:

          return (0, 0, 0)

        if b == 0:

          return (a // abs(a), 0, abs(a))

        (u, v, p) = self.bezout(b, a % b)

        return (v, (u - v * (a // b)), p)

    def inv_modulo(self, x, m):

      (u, _, p) = self.bezout(x, m)

      return u % abs(m)

class Wiener(object):

    def division_euclidienne(self, a, b):

      return (a // b, a % b)

    def fraction_continue(self, n, d):

      developpement = []
      a = n
      b = d

      while b != 0:

        (q,r) = self.division_euclidienne(a,b)

        developpement.append(q)

        a = b
        b = r

      return (developpement)

    def reduites_fraction_continue(self, a):

      l=len(a)

      reduites=[]

      h0 = 1
      h1 = 0
      k0 = 0
      k1 = 1

      count = 0

      while count < l:

        h = a[count] * h1 + h0
        h0 = h1
        h1 = h

        k = a[count] * k1 + k0
        k0 = k1
        k1 = k

        reduites.append((k,h))

        count += 1

      return (reduites)

    def wiener(self, n, e):

      fc = self.fraction_continue(e, n)

      reduites = self.reduites_fraction_continue(fc)

      message_clair = random.randint(10**1,10**5)

      message_chiffre = pow(message_clair, e, n)

      l = len(reduites)

      i = 0

      while(i < l and pow(message_chiffre, reduites[i][1], n) != message_clair):
      
            i += 1

      if i != l:

        return (reduites[i][1])

      else:

        print("\t\033[1;31m[-]\033[0m Not a valid RSA key for Wiener Attack\n")
        exit(0)
        

def prime_factorize(n):
    factors = []
    number = math.fabs(n)
    while number > 1:
        factor = get_next_prime_factor(number)
        factors.append(factor)
        number /= factor
    if n < -1:
        factors[0] = -factors[0]
    return tuple(factors)
    
def get_next_prime_factor(n):
    if n % 2 == 0:
        return 2
    for x in range(3, int(math.ceil(math.sqrt(n)) + 1), 2):
        if n % x == 0:
            return x
    return int(n)
    
    
def encryptRSA(plain, publickey, etype):


    rsa_key = RSA.importKey(publickey)
    rsa_key = PKCS1_OAEP.new(rsa_key)
    plain = zlib.compress(plain)
    encrypted = rsa_key.encrypt(plain)

    if etype == 'base64':
    
        encrypted = base64.b64encode(encrypted)
    
    
    elif etype == 'hex':
    
        encrypted = encrypted.encode('hex')
    
    elif etype == 'decimal':
    
        encrypted = bytes_to_long(encrypted)
    
    elif etype == 'raw':
    
        encrypted = encrypted
        
    else:
    
        print('\033[1;31m[-]\033[0m An error ocurred')
        
    return encrypted



def decryptRSA(ciphertext, privatekey):

    rsakey = RSA.importKey(privatekey)
    rsakey = PKCS1_OAEP.new(rsakey)
    
    if etype == 'base64':
    
        decrypted = base64.b64decode(decrypted)
    
    
    elif etype == 'hex':
    
        decrypted = encrypted.decode('hex')
    
    elif etype == 'decimal':
    
        decrypted = long_to_bytes(ciphertext)
    
    elif etype == 'raw':
    
        decrypted = ciphertext
        
    else:
    
        print('\033[1;31m[-]\033[0m An error ocurred')
    
    
    decrypted = rsakey.decrypt(decrypted)
    out = zlib.decompress(decrypted)
    
    return out



def signRSA(message, privatekey, hashAlg):

    global hash1
    hash1 = hashAlg
    signer = PKCS1_v1_5.new(privatekey)
    if (hash1 == "SHA-512"):
        digest = SHA512.new()
    elif (hash1 == "SHA-384"):
        digest = SHA384.new()
    elif (hash1 == "SHA-256"):
        digest = SHA256.new()
    elif (hash1 == "SHA-1"):
        digest = SHA.new()
    else:
        digest = MD5.new()
    digest.update(message)
    return signer.sign(digest)

def verifyRSA(message, signature, publickey):

    signer = PKCS1_v1_5.new(publickey)
    if (hash1 == "SHA-512"):
        digest = SHA512.new()
    elif (hash1 == "SHA-384"):
        digest = SHA384.new()
    elif (hash1 == "SHA-256"):
        digest = SHA256.new()
    elif (hash1 == "SHA-1"):
        digest = SHA.new()
    else:
        digest = MD5.new()
    digest.update(message)
    return signer.verify(digest, signature)

def extractPub(key):
    key=RSA.importKey(key)
    n,e = key.n, key.e
    print("\n\t\033[1;32m[+]\033[0m Modulus: {}".format(str(n)))  
    print("\n\t\033[1;32m[+]\033[0m Exponent: {}".format(str(e)))


def extractPriv(key):
    key=RSA.importKey(key)
    n,e,d,p,q = key.n, key.e, key.d, key.p, key.q
    print("\n\t\033[1;32m[+]\033[0m Modulus: {}".format(str(n)))  
    print("\n\t\033[1;32m[+]\033[0m Public Exponent: {}".format(str(e)))   
    print("\n\t\033[1;32m[+]\033[0m Private Exponent: {}".format(str(d)))   
    print("\n\t\033[1;32m[+]\033[0m p factor: {}".format(str(p)))   
    print("\n\t\033[1;32m[+]\033[0m q factor: {}".format(str(q)))



def embedPub(n, e):
    n = bytes_to_long(long_to_bytes(n))
    e = bytes_to_long(long_to_bytes(e))
    rsaobj = RSA.construct((n,e))
    key = rsaobj.exportKey().decode('utf-8')
    return key


def embedPriv(p, q, e):
    p = bytes_to_long(long_to_bytes(p))
    q = bytes_to_long(long_to_bytes(q))
    e = bytes_to_long(long_to_bytes(e))
    n = p * q
    n = bytes_to_long(long_to_bytes(n))
    phi = (p - 1) * (q - 1)
    d = gmpy2.invert(e, phi)
    d = bytes_to_long(long_to_bytes(d))
    key = RSA.construct((n,e,d,p,q))
    key = RSA._RSAobj.exportKey(key).decode('utf-8')
    return key

def RSAsolverpqec(p, q, e, c):

    print('\033[1;34m[*]\033[0m Calculating Plain-Text')
    n = int(p) * int(q)
    
    phi = (int(p) - 1) * (int(q) - 1)
    
    d = gmpy2.invert(int(e), phi)
    
    m = pow(int(c),int(d),int(n))
    
    return m
    
def RSAsolverndc(n, d, c):

    print('\033[1;34m[*]\033[0m Calculating Plain-Text')
    m = fast_exp(c,d) % n
    return m




def fermatAttack(n, e):
    try:
        (p, q) = Fermat.fermat(n, e)
    except:
        print("\n\033[1;31m[-]\033[0m This RSA key is not valid for a Fermat Attack\n")
        exit()
        phi = indicatrice_euler(p,q)
        d = gmpy2.invert(e, phi)       
        return d

def wienerAttack(n, e):
    d = Wiener.wiener(n, e)
    return d

def smallN(n):

    p = prime_factorize(n)
    print('\033[1;34m[*]\033[0m Starting N factorization...')
    print('\033[1;32m[+]\033[0m DONE! N Factorized:')
    print('\t\033[1;34m[*]\033[0m p = ' + str(p[0]))
    print('\t\033[1;34m[*]\033[0m q = ' + str(p[1]))

def genKeys(bits):

    print('\033[1;34m[*]\033[0m Generating keys of ' + bits + ' bits.')
    random_generator = Random.new().read
    key = RSA.generate(int(bits), random_generator)
     
    privatekey = key.exportKey("PEM")
    publickey = key.publickey().exportKey("PEM")
    
    keys = [privatekey, publickey]
    
    return keys

def nemEncrypt(n, e, m):

    c = fast_exp(m,e) % n
    
    return c


def pqemEncrypt(p,q,e,m):
    n = p * q
    c = fast_exp(m,e) % n    
    return c


def genOps(m, bits):

    print('\033[1;34m[*]\033[0m Generating primes')
    
    
    p = getPrime(int(bits))
    print('\033[1;34m[*]\033[0m p = ' + str(p))
    q = getPrime(int(bits))
    print('\033[1;34m[*]\033[0m q = ' + str(q))

    n = p * q
    
    print('\033[1;34m[*]\033[0m n = ' + str(n))
    
    phi = (p - 1) * (q - 1)
    
    print('\033[1;34m[*]\033[0m phi = ' + str(phi))
    a = 2
    while a == 2:
        try:
            e = randint(1, phi)
            d = gmpy2.invert(e,phi)
            a = 0
        except:
            a = 2
    print('\033[1;34m[*]\033[0m e = ' + str(e))
    print('\033[1;34m[*]\033[0m d = ' + str(d))
    
    c = pow(m,e,n)
    
    print('\033[1;34m[*]\033[0m c = ' + str(c))
    
    return c


def hastadAttack(n0, n1, n2, e, c0, c1, c2):


    print("\n\033[1;32m[+]\033[0m Modular inverse calculation...")

    b0,b1,b2 = Hastad.xgcd(n0,n1*n2)[2], Hastad.xgcd(n1,n0*n2)[2], Hastad.xgcd(n2,n0*n1)[2]

    print("\033[1;32m[+]\033[0m Modular inverse calculation done...")

    print("\n\033[1;32m[+]\033[0m System solution cube calculation...")

    m=(b0 * c0 * n1 * n2) + (b1 * c1 * n0 * n2) + (b2 * c2 * n0 * n1)
    m %= (n0 * n1 * n2)

    print("\033[1;32m[+]\033[0m System solution cube calculation done")

    print("\n\033[1;32m[+]\033[0m System solution calculation...")

    x = Hastad.root(m,e)[0]

    print("\033[1;32m[+]\033[0m System solution calculation done")

    print("\n\033[1;32m[+]\033[0m Solution interpretation...")

    p = codecs.decode(hex(x)[2:].replace('L',''),"hex_codec").decode('utf-8')

    print("\033[1;32m[+]\033[0m Solution interpretation done")

    print("\n\033[1;32m[+]\033[0m The plaintext is: {}".format(p.replace('\n','\n\t\t')))


def commonModulus(n, e1, e2, c1, c2):

      Comod.accueil()

      egcd = Comod.xgcd(e1, e2)
      u, v = egcd[1], egcd[2]

      if u >= 0:

        p1 = Comod.pow_mod(c1,u,n)

      else:

        p1 = Comod.modinv(Comod.pow_mod(c1,-u,n),n)

      if v >= 0:

        p2 = Comod.pow_mod(c2,v,n)

      else:

        p2 = Comod.modinv(Comod.pow_mod(c2,(-v),n),n)

      res = (p1 * p2) % n

      print ("\033[1;32m[+]\033[0m Decimal plaintext: " + res + "\n")

      try:

        plaintext = codecs.decode(hex(res)[2:].replace('L',''), "hex_codec").decode('utf-8')

        print ("\033[1;32m[+]\033[0m Interpreted plaintext: " + plaintext + "\n")

      except:

        print("\033[1;31m[-]\033[0m Non-interpretable plaintext\n")

