#!/data/data/com.termux/files/usr/bin/bash

#MOVE LFS OUT TO REPO 
echo "Saving LFS files to repo directory..."
mv openjdk-21_21.1.1-1_aarch64.deb ../

#ACTUALIZA DEB FILES AL ARBOL DE DIRECTORIOS
termux-apt-repo . . stable extras

#RETURN LFS FILES 
echo "Recovering LFS files to repo directory..."
mv ../openjdk-21_21.1.1-1_aarch64.deb .

#CREAMOS EL FILE Packages.gz
#pushd dists/stable/extras/binary-all/
#gzip -k -f Packages
# FIRMA DE REPOSITORIES
#cd ../../
#gpg --default-key "ivam3.bh@gmail.com" -abs -o - Release > Release.gpg
#gpg --default-key "ivam3.bh@gmail.com" --clearsign -o - Release > InRelease
#popd

#         @Ivam3
