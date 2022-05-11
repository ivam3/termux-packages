#!/usr/bin/bash

[[ -e files.json ]] && rm files.json
touch files.json

find home -type f > files.txt
declare -a files=$(cat files.txt)

for i in ${files[*]}
do
	echo "+$i+: +$i+" >> files.json
done
sed -i 's|+|"|g' files.json
rm files.txt
cat files.json
