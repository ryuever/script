#!/bin/bash

srcdir="$HOME/Dropbox/org"
desdir="$HOME/Google Drive/org/org$(date +%Y%m%d).rar"

echo "$desdir"
echo $desdir
tar -zcvf "$desdir" $srcdir
