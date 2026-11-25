unction Hello {
  echo "Hello"
}

Hello
function ntmy {
  echo "nice to  meet you $1"
}
ntmy
function add_sum{
  sum=0

  for item in $@
  do
    let sum=sum+$item
  done
  echo $sum
}
add_sum
source writing_functions.sh
ntmy udit
ntmy sir
ntmy sarubala
