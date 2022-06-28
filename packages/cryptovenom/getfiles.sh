#!/usr/bin/bash

[[ -e files.json ]] && rm files.json
touch files.json

find home -type f > files.txt
declare -a files=$(cat files.txt)

for i in ${files[*]}
do
	echo -en "\t\t+$i+: +/data/data/com.termux/files/$i+\n" >> files.json
done
sed -i 's|+|"|g' files.json
sed -i 's|$|,|g' files.json
ln=$(wc -l files.json|awk -F " " '{print $1}')
sed -i "$ln {s/,/ /}" files.json
rm files.txt

cat <<- EOF > manifiest.json
{
  "name": "cryptovenom",
  "version": "1.0.1",
  "arch": "all",
  "homepage": "https://https://github.com/lockedbyte/cryptovenom",
  "maintainer": "Ivam3 <https://t.me/Ivam3_Bot>",
  "depends": ["python2"],
  "suggests": ["i-haklab"],
  "description": "OpenSource tool which contains a lot of cryptosystems and cryptoanalysis methods all in one.",
  "files" :{
    "cryptovenom-installer": "bin/cryptovenom-installer",
    "cryptovenom": "bin/cryptovenom",
		$(cat files.json)
  }
}
EOF
rm files.json 2>/dev/null
