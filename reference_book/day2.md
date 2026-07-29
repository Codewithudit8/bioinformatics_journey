problem : finding k mer sequence in a given taxt 
output : count the number of kmer appear in the text
pseudocode:
PATTERNCOUNT(Text, Pattern)
count 0
for i 0 to |Text| ! |Pattern|
if Text(i, |Pattern|) = Pattern
count count + 1
return count
