#PREINST
## It take effect after installation and if prerm failed or if process is aborted.

#POSTRM
# If process is aborting :

#PRERM
## It takes action before package be removed and if theres some conflict with dpkg

#PREINST 
# It take effect before installation and in upgrade process

#Creating a GPG key
#Install gpg and create a new key:

apt install gnupg
gpg --full-gen-key
#Use RSA:

#Please select what kind of key you want:
#   (1) RSA and RSA (default)
#   (2) DSA and Elgamal
#   (3) DSA (sign only)
#  (4) RSA (sign only)
#Your selection? 1
#RSA with 4096 bits:

#RSA keys may be between 1024 and 4096 bits long.
#What keysize do you want? (3072) 4096

#backup your private key using:
gpg --export-secret-keys "${EMAIL}" > my-private-key.asc

#And import it using:
gpg --import my-private-key.asc

#Create the ASCII public key file KEY.gpg inside the git repo my_ppa:
gpg --armor --export "${EMAIL}" > /path/to/my_ppa/KEY.gpg
#Note: The private key is referenced by the email address you entered in the previous step.

#Creating the Packages and Packages.gz files
#Inside the git repo my_ppa:
apt install dpkg-scanpackages
dpkg-scanpackages --multiversion . > Packages
gzip -k -f Packages

#Creating the Release, Release.gpg and InRelease files
#Inside the git repo my_ppa:
apt install apt-ftparchive
apt-ftparchive release . > Release
gpg --default-key "${EMAIL}" -abs -o - Release > Release.gpg
gpg --default-key "${EMAIL}" --clearsign -o - Release > InRelease

#Creating the my_list_file.list file
#Inside the git repo my_ppa:
echo "deb https://${GITHUB_USERNAME}.github.io/my_ppa ./" > my_list_file.list

#This file will be installed later on in the user’s /etc/apt/sources.list.d/ directory. This tells apt to look for updates from your PPA in https://${GITHUB_USERNAME}.github.io/my_ppa.

#Now you can tell all your friends and users to install your PPA this way:
curl -s --compressed "https://${GITHUB_USERNAME}.github.io/my_ppa/KEY.gpg" | sudo apt-key add - curl -s --compressed -o /etc/apt/sources.list.d/my_list_file.list "https://${GITHUB_USERNAME}.github.io/my_ppa/my_list_file.list"
apt update

#How to add new packages
#Just put your new .deb files inside the git repo my_ppa and execute:
# Packages & Packages.gz
dpkg-scanpackages --multiversion . > Packages
gzip -k -f Packages

# Release, Release.gpg & InRelease
apt-ftparchive release . > Release
gpg --default-key "${EMAIL}" -abs -o - Release > Release.gpg
gpg --default-key "${EMAIL}" --clearsign -o - Release > InRelease
# Commit & push



