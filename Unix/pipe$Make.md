dell@DESKTOP-RO81QOS:~$ ##  Use pipes to figure out how many US states contain the word “New.”

Examine your ~/.bash_history to try to figure out how many unique commands you’ve ever used. (You may need to look up how to use the uniq and sort commands).

-bash: syntax error near unexpected token `('
dell@DESKTOP-RO81QOS:~$ grep "New" states.txt | wx -l
wx: command not found
dell@DESKTOP-RO81QOS:~$ grep "New" states.txt | wc -l
4
dell@DESKTOP-RO81QOS:~$ sort ~/.bash_history | uniq | wc -l
322
### installed and worked
dell@DESKTOP-RO81QOS:~/document$ cd Journal
dell@DESKTOP-RO81QOS:~/document/Journal$ nano makefile
dell@DESKTOP-RO81QOS:~/document/Journal$ ls
makefile
dell@DESKTOP-RO81QOS:~/document/Journal$ make
touch draft_journal_entry.txt
dell@DESKTOP-RO81QOS:~/document/Journal$ ls
draft_journal_entry.txt  makefile
dell@DESKTOP-RO81QOS:~/document/Journal$ make draft_journal_entry.txt
make: 'draft_journal_entry.txt' is up to date.
dell@DESKTOP-RO81QOS:~/document/Journal$ echo " 23sept-2026" > toc.txt
dell@DESKTOP-RO81QOS:~/document/Journal$ nano makefile
dell@DESKTOP-RO81QOS:~/document/Journal$ make readme.txt
echo "this journal contains the follwing number :" > readme.txt
wc -l toc.txt | egrep -o "[0-9]+" >> readme.txt
dell@DESKTOP-RO81QOS:~/document/Journal$ cat readme.txt
this journal contains the follwing number :
1
dell@DESKTOP-RO81QOS:~/document/Journal$ make readme.txt
make: 'readme.txt' is up to date.
dell@DESKTOP-RO81QOS:~/document/Journal$ echon "2 . 2026-09-24-talk" >> toc.txt
Command 'echon' not found, did you mean:
  command 'echo' from deb coreutils-from-gnu (0.0.0~ubuntu25)
  command 'echo' from deb coreutils-from-uutils (0.0.0~ubuntu25)
  command 'echo' from deb coreutils-from-busybox (0.0.0~ubuntu25)
  command 'echo' from deb coreutils-from-toybox (0.0.0~ubuntu25)
Try: sudo apt install <deb name>
dell@DESKTOP-RO81QOS:~/document/Journal$ echo "2 . 2026-09-24-t
alk" >> toc.txt
dell@DESKTOP-RO81QOS:~/document/Journal$ make readme.txt
echo "this journal contains the follwing number :" > readme.txt
wc -l toc.txt | egrep -o "[0-9]+" >> readme.txt
dell@DESKTOP-RO81QOS:~/document/Journal$ cat readme.txt
this journal contains the follwing number :
2
dell@DESKTOP-RO81QOS:~/document/Journal$
