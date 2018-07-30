#! /bin/bash

dirc="16/"
init="Q"
obj="obj/"

file=$(ls $dirc)

for filename in $file
do
#  echo $dirc$filename
#  echo $dirc$init$filename
#  echo $dirc"C"${filename%.*}
  exec="mv "$dirc$filename" "$obj$init$filename
  $exec
  echo $dirc$init$filename" is ok!" 
done
