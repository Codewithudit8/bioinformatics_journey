#!/usr/bin/env bash
echo {0..9}
echo A{1..9}
echo a{1..9}c
echo {1..3}{A..C}
start=1
end=10
echo {$start..$end}
eval echo {$start..$end}
echo {{1..5},{a..e}}
echo {who,what,when,where,how}?
echo {udit}{sahoo}
echo {udit}+{sahoo}
echo "for loop"
for i in {1..5}
do
  echo "i is equal to $i"
done
echo "after loop"
echo "explicit list"
for i in states.txt
do
  echo {"$i"}
done
long=(greate indian fighter)
for i in ${long[*]}
do
  echo "$i"
done
for demo in $(ls)
do
