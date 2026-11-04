echo "revision_4thoct"
sequence=(ATCGGCTA ATGCTCAT GTCAGACGT)
sequence[1]=TCGCTAGC
echo ${sequence[*]}
echo ${sequence[1]}
plagues=(blood frogs lice flies sickness boils hail)
echo ${#plagues[*]}
echo ${plagues[*]:2:6}
echo ${plagues[*]:0:2}
team_a=(1 2 3)
team_b=(4 5)
team_b+=(6 7)
echo ${team_b[*]}
result=$((${#team_a[*]}+${#team_b[*]}))
echo $result
count=5
while [[ $count -gt 0 ]]
do
  echo " the number is $count "
  let count=$count-1
done
echo "count has finished"
