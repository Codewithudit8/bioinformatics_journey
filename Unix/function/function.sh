echo  "27 nov revision"
for number in {1..10}
  do
    if [[ $number -lt 3 ]] || [[ $number -gt 8 ]]
    then
      echo $number
    fi
  done
echo "while revsion"
#!/usr/bin/env bash
count=3
while [[ $count -gt 0 ]]
  do
    echo "the numbers are : $count"
    let count=$count-1
  done
echo "for loop revision"
echo "printing content of an array"
dna=(ATCGC TGACGC GCATGTCA)
for i in ${dna[*]}
  do
    echo "the sequence in dna are : $i"
  done
for i in $(ls)
 do
   echo "recent files are : $i"
 done
echo "braces"
start=1
end=9
echo {$start..$end}
eval echo {$start..$end}
echo {1..10}{A..J}
echo {{1..10},{A..C}}
echo "newly learnt 27 nov:"
function cal_sum {
  sum=0
  for i in $@
  do
    let sum=sum+i
  done
  echo $sum
}

function cal_sum1 {
  local sum=0
  for i in $@
  do
    let sum=sum+i
  done
  echo $sum

}
function plier {
  local mul=1
  for i in $@
  do
    let mul=mul*i
     done
  echo $mul
}

function isiteven {
  if [[ $(($1 % 2 )) -eq 0 ]]
  then
    echo 1
  else
    echo 2
  fi
}
