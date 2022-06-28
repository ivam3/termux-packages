#!/usr/bin/python


#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
#                    [====={ CRYPTO VENOM SETUP }=====]
#
#    | WELCOME TO THE /** CRYPTOVENOM FRAMEWORK SETUP **/ |
#
#              ( https://github.com/lockedbyte/cryptovenom )
#
#           << GNU PUBLIC LICENSE >>
#
#                               -/ CREATED BY LOCKEDBYTE /-
#
#                 - [ CONTACT => alejandro.guerrero.rodriguez2@gmail.com ] -
#                 - [ CONTACT => @LockedByte (Twitter) ] -
#
#
# AND NOW...HERE THE CODE
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#


import commands,sys,os
user = commands.getoutput('whoami')
if not user == 'root':
    print('[ERR] Root permissions needed to install CryptoVenom!')
    exit(1)
print('[INFO] Checking for main file')
a = True
try:
    open('cryptovenom.py', 'r')
except:
    a = False

if(a):
    print('[INFO] Main file found, skipping...')
else:
    print('[INFO] Copying main file...')
    os.system('cp aux/cryptovenom.py cryptovenom.py')
    os.system('sudo chmod 777 cryptovenom.py')
print('[INFO] Exec: sudo apt-get update')
os.system('sudo apt-get update')
print('[INFO] Installing apt-get based dependencies...')
os.system('sudo apt-get install libgmp-dev libmpfr-dev libmpc-dev build-essential libssl-dev python-dev')

print('[INFO] Installing pip requirements via -> requirements.txt')
os.system('sudo pip install -r requirements.txt')

print('[DONE] CryptoVenom dependencies installed sucessfully!')
print('[WARN] If you find any error, or problem while using CryptoVenom or problems with one of it\'s dependencies contact me through Telegram (@LockedByte), email (alejandro.guerrero.rodriguez2@gmail.com) or open it in GitHub. Enjoy!')


