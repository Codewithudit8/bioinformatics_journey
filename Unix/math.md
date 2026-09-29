## some basic math function 
dell@DESKTOP-RO81QOS:~$ expr 5+2
5+2
dell@DESKTOP-RO81QOS:~$ expr 5-2
5-2
dell@DESKTOP-RO81QOS:~$ expr 5 + 2
7
dell@DESKTOP-RO81QOS:~$ expr 5 - 2
3
dell@DESKTOP-RO81QOS:~$ expr \* 2
expr: syntax error: unexpected argument '2'
dell@DESKTOP-RO81QOS:~$ expr \ * 2
expr: syntax error: unexpected argument '2'
dell@DESKTOP-RO81QOS:~$ expr 5 \* 2
10
dell@DESKTOP-RO81QOS:~$ 5 / 2
5: command not found
dell@DESKTOP-RO81QOS:~$ expr 5 / 2
2
dell@DESKTOP-RO81QOS:~$ bash math.sh
bash: math.sh: No such file or directory
dell@DESKTOP-RO81QOS:~$ touch math.sh
dell@DESKTOP-RO81QOS:~$ bash math.sh
dell@DESKTOP-RO81QOS:~$ nano math.sh
dell@DESKTOP-RO81QOS:~$ bash math.sh
2
10
7
dell@DESKTOP-RO81QOS:~$ nano math.sh
dell@DESKTOP-RO81QOS:~$ bash math.sh
2
10
7
bc -l 5 / 2
dell@DESKTOP-RO81QOS:~$ nano math.sh
dell@DESKTOP-RO81QOS:~$ bash.math.sh
bash.math.sh: command not found
dell@DESKTOP-RO81QOS:~$ bash math.sh
2
10
7
2.50000000000000000000
dell@DESKTOP-RO81QOS:~$ nano math.sh
dell@DESKTOP-RO81QOS:~$ expr 1 % 3
1
dell@DESKTOP-RO81QOS:~$ expr 10 % 3
1
dell@DESKTOP-RO81QOS:~$ nano bigmath.sh
dell@DESKTOP-RO81QOS:~$ bash bigmath.sh
3.14285714285714285714
38.430
38.430
26.20000000000000000000
dell@DESKTOP-RO81QOS:~$
