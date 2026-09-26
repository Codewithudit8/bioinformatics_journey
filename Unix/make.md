## working with make command
dell@DESKTOP-RO81QOS:~$ cd document
dell@DESKTOP-RO81QOS:~/document$ ls
Journal  states.txt
dell@DESKTOP-RO81QOS:~/document$ less journal
journal: No such file or directory
dell@DESKTOP-RO81QOS:~/document$ less Journal
Journal is a directory
dell@DESKTOP-RO81QOS:~/document$ cd journal
-bash: cd: journal: No such file or directory
dell@DESKTOP-RO81QOS:~/document$ cd Journal
dell@DESKTOP-RO81QOS:~/document/Journal$ ls -l
total 12
-rw-r--r-- 1 dell dell   0 Sep 24 15:18 draft_journal_entry.txt
-rw-r--r-- 1 dell dell 194 Sep 24 16:29 makefile
-rw-r--r-- 1 dell dell  46 Sep 24 17:01 readme.txt
-rw-r--r-- 1 dell dell  33 Sep 24 17:01 toc.txt
dell@DESKTOP-RO81QOS:~/document/Journal$ nano makefile
dell@DESKTOP-RO81QOS:~/document/Journal$ nano makefile
dell@DESKTOP-RO81QOS:~/document/Journal$ make clean
makefile:8: warning: overriding recipe for target 'draft_journal_entry.txt'
makefile:2: warning: ignoring old recipe for target 'draft_journal_entry.txt'
makefile:10: warning: overriding recipe for target 'readme.txt'
makefile:4: warning: ignoring old recipe for target 'readme.txt'
rm draft_journal_.txt
rm: cannot remove 'draft_journal_.txt': No such file or directory
make: *** [makefile:13: clean] Error 1
dell@DESKTOP-RO81QOS:~/document/Journal$ nano makefile
dell@DESKTOP-RO81QOS:~/document/Journal$ make clean
rm draft_journal_.txt
rm: cannot remove 'draft_journal_.txt': No such file or directory
make: *** [makefile:8: clean] Error 1
dell@DESKTOP-RO81QOS:~/document/Journal$ make
make: Nothing to be done for 'all'.
dell@DESKTOP-RO81QOS:~/document/Journal$ nano makefile
dell@DESKTOP-RO81QOS:~/document/Journal$ make clean
rm draft_journal_entry.txt
rm readme.txt
dell@DESKTOP-RO81QOS:~/document/Journal$ ls
makefile  toc.txt
