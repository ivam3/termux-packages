#!/data/data/com.termux/files/usr/bin/bash

#ACTUALIZA DEB FILES AL ARBOL DE DIRECTORIOS
termux-apt-repo . . stable extras

#CREAMOS EL FILE Packages.gz
#pushd dists/stable/extras/binary-all/
#gzip -k -f Packages
# FIRMA DE REPOSITORIES
#cd ../../
#gpg --default-key "ivam3.bh@gmail.com" -abs -o - Release > Release.gpg
#gpg --default-key "ivam3.bh@gmail.com" --clearsign -o - Release > InRelease
#popd

#         @Ivam3
