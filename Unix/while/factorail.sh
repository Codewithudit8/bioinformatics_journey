#!/usr/bin/env bash
count=3
while [[ $count -gt 0 ]]
do
  echo "count is equal to $count"
  let count=$count-1
done
fact=1
num=5
temp=$num
while [[ $temp -gt 1 ]]
do
  fact=$((fact * temp))
  temp=$((temp - 1))
done
echo "the factorail is :"$fact
echo "revision_30ct"
heroes=(ironman batman superman flash thor hulk)
echo ${heroes[0]}
echo ${heroes[3]}
echo ${heroes[*]}
echo ${#heroes[*]}
heroes+=(wolverine deadpool)
echo "Final Heroes :${heroes[*]}"
echo "new length : ${#heroes[*]}"
villains=(jocker thanos venom)
sum=$((${#heroes[*]}+${#villains[*]}))
echo $sum
