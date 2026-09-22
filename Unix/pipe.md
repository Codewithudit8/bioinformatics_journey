dell@DESKTOP-RO81QOS:~$ nano canada.txt
dell@DESKTOP-RO81QOS:~$ cd ~/document
dell@DESKTOP-RO81QOS:~/document$ cat canada.txt
cat: canada.txt: No such file or directory
dell@DESKTOP-RO81QOS:~/document$ cd ..
dell@DESKTOP-RO81QOS:~$ cat canada.txt | head -n 5
Nunavut
## Quebec
## Northwest Territories
## Ontario
## British Columbia
dell@DESKTOP-RO81QOS:~$ grep "[aeiou]$" states.txt | wc -l
32
dell@DESKTOP-RO81QOS:~$ ls -al | grep "Feb" | less
dell@DESKTOP-RO81QOS:~$ grep "*a*" states.txt | wc -l
0
dell@DESKTOP-RO81QOS:~$ grep "a*" states.txt | wc -l
50
dell@DESKTOP-RO81QOS:~$ egrep "a*" states.txt  | wc -l
50
dell@DESKTOP-RO81QOS:~$ less states.txt | wc -l
50
dell@DESKTOP-RO81QOS:~$  wc -l | less states.txt
