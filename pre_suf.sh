#!/bin/bash
prefix="<li>"
suffix="</li>"
file="shell.org"
while read -r line
do
 echo "${prefix}$line${suffix}"
done <$file > temp
mv temp $file
