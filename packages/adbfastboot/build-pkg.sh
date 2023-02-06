#!/data/data/com.termux/files/usr/bin/bash
#armeabi-v7a, x86 and x86-64 are supported on arm64-v8a
#x86 is supported on armeabi-v7a
IFS=$'\n\t'

for debarch in arm i686 aarch64 x86_64; do
  [[ "$debarch" == "aarch64" ]] && { arch="arm64-v8a" ;}
  [[ "$debarch" == "arm" ]] && { arch="armeabi-v7a" ;}
  [[ "$debarch" == "x86_64" ]] && { arch=$debarch ;}
  [[ "$debarch" == "i686" ]] && { arch="x86" ;}
  v=$(grep version manifiest.json.all|awk -F ":" '{print $2}'|tr -d ","|tr -d " "|tr -d "\"")
  debpkg="adbfastboot_${v}_${arch}.deb"
  echo "[-] Delelating old deb package."
  [[ -e /storage/0095-4180/Android/data/com.termux/files/Ivam3/repositories/termux-packages/$debpkg ]] && {
    rm /storage/0095-4180/Android/data/com.termux/files/Ivam3/repositories/termux-packages/$debpkg
  }
  echo "[*] Creating manifiest."
  cp manifiest.json.all manifiest.json
  echo "[*] Set architecture $arch."
  sed -i "s|debarch|$debarch|g" manifiest.json
  sed -i "s|all|$arch|g" manifiest.json
  echo "[+] Building deb for $arch"
  termux-create-package manifiest.json
  rm manifiest.json
done
echo "[*] Moving debs to termux-packages proyect."
mv *.deb /storage/0095-4180/Android/data/com.termux/files/Ivam3/repositories/termux-packages/
echo "[*] DONE."
