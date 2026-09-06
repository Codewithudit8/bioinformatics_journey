# nano,cat,redirection,crating directory in home with out switching directories
dell@DESKTOP-RO81QOS:~$ cat ~/workbench/readme.txt
1
2
3
dell@DESKTOP-RO81QOS:~$ cat readme.txt
dell@DESKTOP-RO81QOS:~$ cat ~/workbench/readme.txt
1
2
3
dell@DESKTOP-RO81QOS:~$ pwd
/home/dell
dell@DESKTOP-RO81QOS:~$ cd workbench
dell@DESKTOP-RO81QOS:~/workbench$ cat readme.txt
1
2
3
dell@DESKTOP-RO81QOS:~/workbench$ cd ..
dell@DESKTOP-RO81QOS:~$ pwd
/home/dell
dell@DESKTOP-RO81QOS:~$ ls ~ > ~/workbench/list.txt
dell@DESKTOP-RO81QOS:~$ wc -m ~/workbench/list.txt
128 /home/dell/workbench/list.txt
dell@DESKTOP-RO81QOS:~$ wc -l ~/workbench/list.txt
12 /home/dell/workbench/list.txt
dell@DESKTOP-RO81QOS:~$ wc -w ~/workbench/list.txt
