## copy and move 
## dispalying file content from one directory to other


dell@DESKTOP-RO81QOS:~/current_unix$ ls
math.sh  vars.sh
dell@DESKTOP-RO81QOS:~/current_unix$ mv current_unix/math.sh dell/temp
mv: cannot stat 'current_unix/math.sh': No such file or directory
dell@DESKTOP-RO81QOS:~/current_unix$ cp math.sh /temp
cp: cannot create regular file '/temp': Permission denied
dell@DESKTOP-RO81QOS:~/current_unix$ cp math.sh /dell
cp: cannot create regular file '/dell': Permission denied
dell@DESKTOP-RO81QOS:~/current_unix$ sudo cp math.sh /temp
dell@DESKTOP-RO81QOS:~/current_unix$ ls /temp
/temp
dell@DESKTOP-RO81QOS:~/current_unix$ ls -f / temp
ls: cannot access 'temp': No such file or directory
/:
.   run   lib64  wslJiDCOn  wslEnHGLn  snap  wsldLEnKn  media  tmp   mnt        root  srv   bin         wslobBFBl  usr
..  init  dev    home       proc       sys   opt        lib    temp  wslPGKHGn  etc   sbin  lost+found  boot       var
dell@DESKTOP-RO81QOS:~/current_unix$ ls -f /temp
/temp
dell@DESKTOP-RO81QOS:~/current_unix$ ls /temp
/temp
dell@DESKTOP-RO81QOS:~/current_unix$ cd dell
-bash: cd: dell: No such file or directory
dell@DESKTOP-RO81QOS:~/current_unix$ cd ..
dell@DESKTOP-RO81QOS:~$ cd temp
dell@DESKTOP-RO81QOS:~/temp$ ls
 file4.txt   file5.txt  'hey there'
dell@DESKTOP-RO81QOS:~/temp$ cd dell
-bash: cd: dell: No such file or directory
dell@DESKTOP-RO81QOS:~/temp$ cd ..
dell@DESKTOP-RO81QOS:~$ cd current_unix
dell@DESKTOP-RO81QOS:~/current_unix$ sudo cp math.sh/temp
cp: missing destination file operand after 'math.sh/temp'
Try 'cp --help' for more information.
dell@DESKTOP-RO81QOS:~/current_unix$ sudo cp math.sh ./temp
dell@DESKTOP-RO81QOS:~/current_unix$ ls /temp
/temp
dell@DESKTOP-RO81QOS:~/current_unix$ ls ./temp
./temp
dell@DESKTOP-RO81QOS:~/current_unix$ ls ../temp
 file4.txt   file5.txt  'hey there'
dell@DESKTOP-RO81QOS:~/current_unix$ cp math.sh ./temp
cp: cannot create regular file './temp': Permission denied
dell@DESKTOP-RO81QOS:~/current_unix$ sudo cp math.sh ../temp
dell@DESKTOP-RO81QOS:~/current_unix$ ls ../temp
 file4.txt   file5.txt  'hey there'   math.sh
dell@DESKTOP-RO81QOS:~/current_unix$ ls
math.sh  temp  vars.sh
dell@DESKTOP-RO81QOS:~/current_unix$ cp vars.sh ../temp
dell@DESKTOP-RO81QOS:~/current_unix$ ls ../temp
 file4.txt   file5.txt  'hey there'   math.sh   vars.sh
dell@DESKTOP-RO81QOS:~/current_unix$ ls
math.sh  temp  vars.sh
dell@DESKTOP-RO81QOS:~/current_unix$ touch demo.txt
dell@DESKTOP-RO81QOS:~/current_unix$ mv demo.txt ../temp
dell@DESKTOP-RO81QOS:~/current_unix$ ls ../temp
 demo.txt   file4.txt   file5.txt  'hey there'   math.sh   vars.sh
dell@DESKTOP-RO81QOS:~/current_unix$ ls -f ../temp
 .   ..  'hey there'   file4.txt   vars.sh   demo.txt   math.sh   file5.txt
dell@DESKTOP-RO81QOS:~/current_unix$ ls -f -h ../temp
 .   ..  'hey there'   file4.txt   vars.sh   demo.txt   math.sh   file5.txt
dell@DESKTOP-RO81QOS:~/current_unix$ mkdir -p ../new_learned ../today
dell@DESKTOP-RO81QOS:~/current_unix$ cd today
-bash: cd: today: No such file or directory
dell@DESKTOP-RO81QOS:~/current_unix$ cd new_learned
-bash: cd: new_learned: No such file or directory
dell@DESKTOP-RO81QOS:~/current_unix$ ls
math.sh  temp  vars.sh
dell@DESKTOP-RO81QOS:~/current_unix$ mkdir -p ../project/data ../project/results
dell@DESKTOP-RO81QOS:~/current_unix$ ls
math.sh  temp  vars.sh
dell@DESKTOP-RO81QOS:~/current_unix$ ls -f
.  ..  vars.sh  temp  math.sh
dell@DESKTOP-RO81QOS:~/current_unix$ ls ../dell
ls: cannot access '../dell': No such file or directory
dell@DESKTOP-RO81QOS:~/current_unix$ ls ./dell
ls: cannot access './dell': No such file or directory
dell@DESKTOP-RO81QOS:~/current_unix$ cd ..
dell@DESKTOP-RO81QOS:~$ ls
 1612671023099.jpg                        bigmath.sh                echofile3.txt   new_lesson      small.txt
 1612671046779.jpg                        bioinformatics_journey    file1           no_a.txt        states.txt
'1612671068880 (2).jpg'                   canada.txt                file2.txt       no_e.txt        states2.txt
'1612671068880 (2).jpg:Zone.Identifier'   current_unix              file3.txt       no_i.txt        states_copy.txt
 1612671068880.jpg                        data_science              file5.txt       no_o.txt        states_copy.txtshahum
 1612671119937.jpg                        document                  four.txt        no_u.txt        temp
 2020                                     draft_journal_entry.txt   journal         phil.txt        today
 2024                                     echo-file2.txt            lab_picture     project         workbanch
 Documents                                echo-file3.txt            makefile        readme.txt      workbench
 Unix                                     echo-file3.txtf           media           revision_unix
 aditya                                   echo-phil.txt             new_learned     small.tx
dell@DESKTOP-RO81QOS:~$ cd ..
dell@DESKTOP-RO81QOS:/home$ cd dell
dell@DESKTOP-RO81QOS:~$ cd new_learned
dell@DESKTOP-RO81QOS:~/new_learned$ ls -f -h
.  ..
dell@DESKTOP-RO81QOS:~/new_learned$ ls -f
.  ..
dell@DESKTOP-RO81QOS:~/new_learned$ ls
dell@DESKTOP-RO81QOS:~/new_learned$ rmdir new_learned
rmdir: failed to remove 'new_learned': No such file or directory
dell@DESKTOP-RO81QOS:~/new_learned$ rm -r new_learned
rm: cannot remove 'new_learned': No such file or directory
dell@DESKTOP-RO81QOS:~/new_learned$ cd ..
dell@DESKTOP-RO81QOS:~$ rm -r new_learned
dell@DESKTOP-RO81QOS:~$ ls -f
 .                   .file4.txt          document            2024                                     draft_journal_entry.txt
 ..                  .git                media               project                                  data_science
 1612671068880.jpg   workbanch           .bash_profile       bioinformatics_journey                   readme.txt
 file3.txt           .file5.txt          1612671046779.jpg   revision_unix                            .motd_shown
 no_o.txt            no_u.txt            no_e.txt            four.txt                                 .ssh
 .git-credentials    .bash_history       .bashrc             small.txt                               '1612671068880 (2).jpg'
 aditya              .local              temp                .lesshst                                 echo-file2.txt
 .cache              echo-phil.txt       canada.txt          workbench                                1612671119937.jpg
 small.tx            .profile            states_copy.txt     2020                                     .bash.profile
 Documents           1612671023099.jpg   current_unix        today                                    echo-file3.txtf
 .gitconfig          states2.txt         echofile3.txt       bigmath.sh                               file5.txt
 phil.txt            makefile            states.txt          new_lesson
 Unix                file2.txt           echo-file3.txt      states_copy.txtshahum
 .bash_logout        file1               lab_picture         .config
 journal             no_i.txt            no_a.txt           '1612671068880 (2).jpg:Zone.Identifier'
dell@DESKTOP-RO81QOS:~$ ls
 1612671023099.jpg                        bigmath.sh                echofile3.txt   no_a.txt        states.txt
 1612671046779.jpg                        bioinformatics_journey    file1           no_e.txt        states2.txt
'1612671068880 (2).jpg'                   canada.txt                file2.txt       no_i.txt        states_copy.txt
'1612671068880 (2).jpg:Zone.Identifier'   current_unix              file3.txt       no_o.txt        states_copy.txtshahum
 1612671068880.jpg                        data_science              file5.txt       no_u.txt        temp
 1612671119937.jpg                        document                  four.txt        phil.txt        today
 2020                                     draft_journal_entry.txt   journal         project         workbanch
 2024                                     echo-file2.txt            lab_picture     readme.txt      workbench
 Documents                                echo-file3.txt            makefile        revision_unix
 Unix                                     echo-file3.txtf           media           small.tx
 aditya                                   echo-phil.txt             new_lesson      small.txt
dell@DESKTOP-RO81QOS:~$
