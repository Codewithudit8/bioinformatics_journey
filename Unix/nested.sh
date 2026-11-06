#!/usr/bin/env bash
for number in {1..3}
do
    for letter in a b
    do
        echo " $number and $letter"
    done
done
num=5
while [[ $num -gt 0 ]]
do
  num1=1
  while [[ $num1 -lt 6  ]]
  do
    echo "the current number is $num$num1"
    num=$(($num + 1))
  done
  num=$(($num1 + 1)
done

