#!/bin/bash

##*************************************************************************************
##   test constructs
##*************************************************************************************
if test -z "$1"
then
  echo "No command-line arguments."
else
  echo "First command-line argument is $1."
fi

if /bin/test -z "$1"
then
  echo "No command-line arguments."
else
  echo "First command-line argument is $1."
fi

if [ -z "$1" ]
then
  echo "No command-line arguments."
else
  echo "First command-line argument is $1."
fi

if /bin/[ -z "$1"]
then
  echo "No command-line arguments."
else
  echo "First command-line argument is $1."
fi

file=/etc/passwd

if [[ -e $file ]]
then
  echo "Password file exists."
fi

if [ -e $file ]
then
  echo "Password file exists."
fi

(( 5 - 5 ))
echo "Exit status of \"(( 5 - 5 )) \" is $?."
