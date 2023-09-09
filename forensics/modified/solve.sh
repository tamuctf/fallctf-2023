#!/bin/bash

for i in ./*.jpeg ; do
	echo $i >> newfiles.txt
done

x=$(sort -V newfiles.txt | cut -c 3-)

rm newfiles.txt

for i in $x ; do
	md5sum $i >> newhashes.txt
done

diff hashes.txt newhashes.txt -y --suppress-common-lines

rm newhashes.txt

