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
echo ""
##*************************************************************************************
##   file test operator
##*************************************************************************************
file="$HOME/Documents/git/script/if_condition.sh"

if [ -r $file ]
then
   echo "File has read access"
else
   echo "File does not have read access"
fi

if [ -w $file ]
then
   echo "File has write permission"
else
   echo "File does not have write permission"
fi

if [ -x $file ]
then
   echo "File has execute permission"
else
   echo "File does not have execute permission"
fi

if [ -f $file ]
then
   echo "File is an ordinary file"
else
   echo "This is sepcial file"
fi

if [ -d $file ]
then
   echo "File is a directory"
else
   echo "This is not a directory"
fi

if [ -s $file ]
then
   echo "File size is zero"
else
   echo "File size is not zero"
fi

if [ -e $file ]
then
   echo "File exists"
else
   echo "File does not exist"
fi
##*************************************************************************************
##   [[]]  vs []
##*************************************************************************************
a="z*"
if [ $a == z* ]
then 
    echo "a is z"
fi

b="z* me"
#  if [ $b == "z* me" ] # too many arguments error
if [[ $b == "z* me" ]]
then 
    echo "b is z \"z* me\""
fi
