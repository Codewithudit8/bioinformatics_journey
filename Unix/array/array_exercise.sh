plagues=(blood frogs lice flies sickness boils hail locusts da>
echo ${plagues[0]}
echo ${plagues[3]}
echo ${plagues[*]}
plagues[4]=disease
echo ${plagues[*]}
echo  ${plagues[*]:5:3}
echo ${#plagues[*]}
plagues+=(satyam sivam sundaram )
echo ${plagues[*]}
plagues[0]=water_fire
echo ${plagues[*]}
echo ${#plagues[*]}
echo "Array exercises"
my_list=(1 2 3 4 5 6)
echo "exercise1"
echo ${my_list[0]}
echo "excercise2"
list1=(1 2 3 4 5)
list2=(5 4 3 2 1)
echo $((${#list1[*]}+${#list2[*]}))
