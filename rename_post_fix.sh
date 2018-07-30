#! /bin/bash

file=$(ls ./JPEGImages/)

for filename in $file
do
#  echo "./JPEGImages/"$filename
#  echo "./JPEGImages/"${filename%.*}
  mv "./JPEGImages/"$filename "./JPEGImages/"${filename%.*}".jpg"
done
