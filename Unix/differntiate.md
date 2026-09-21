dell@DESKTOP-RO81QOS:~/Documents$ cd ..
dell@DESKTOP-RO81QOS:~$ echo -n 4 states.txt > file2.txt
dell@DESKTOP-RO81QOS:~$ less file2.txt
dell@DESKTOP-RO81QOS:~$ head -n 4 states.txt > file2.txt
dell@DESKTOP-RO81QOS:~$ less file.txt
file.txt: No such file or directory
dell@DESKTOP-RO81QOS:~$ less file2.txt
dell@DESKTOP-RO81QOS:~$ head -n 6 states.txt > file3.txt
dell@DESKTOP-RO81QOS:~$ less file3.txt
dell@DESKTOP-RO81QOS:~$ ls
 1612671023099.jpg                        file3.txt
 1612671046779.jpg                        file5.txt
'1612671068880 (2).jpg'                   four.txt
'1612671068880 (2).jpg:Zone.Identifier'   journal
 1612671068880.jpg                        lab_picture
 1612671119937.jpg                        media
 2020                                     no_a.txt
 2024                                     no_e.txt
 Documents                                no_i.txt
 aditya                                   no_o.txt
 data_science                             no_u.txt
 document                                 phil.txt
 echo-file2.txt                           readme.txt
 echo-file3.txt                           small.tx
 echo-file3.txtf                          small.txt
 echo-phil.txt                            states.txt
 echofile3.txt                            temp
 file1                                    workbanch
 file2.txt                                workbench
dell@DESKTOP-RO81QOS:~$ cat file3.txt
Alabama
Alaska
Arizona
Arkansas
California
Colorado
dell@DESKTOP-RO81QOS:~$ diff file2.txt file3.txt
4a5,6
> California
> Colorado
dell@DESKTOP-RO81QOS:~$ sdiff file2.txt file3.txt
Alabama                                                       Alabama
Alaska                                                        Alaska
Arizona                                                       Arizona
Arkansas                                                      Arkansas
                                                              >California
                                                              >Colorado
dell@DESKTOP-RO81QOS:~$ cp states.txt states_copy.txt
dell@DESKTOP-RO81QOS:~$ #### MD5 COMMANDS
dell@DESKTOP-RO81QOS:~$ md5 states.txt
Command 'md5' not found, did you mean:
  command 'mdl' from snap mdl (0.12.0)
  command 'mdu' from deb mtools (4.0.49-1)
See 'snap info <snapname>' for additional versions.
dell@DESKTOP-RO81QOS:~$ sudo apt install md5sum
[sudo: authenticate] Password:
sudo: Authentication failed, try again.
[sudo: authenticate] Password:
Error: Unable to locate package md5sum
dell@DESKTOP-RO81QOS:~$ md5 states.txt
Command 'md5' not found, did you mean:
  command 'mdl' from snap mdl (0.12.0)
  command 'mdu' from deb mtools (4.0.49-1)
See 'snap info <snapname>' for additional versions.
dell@DESKTOP-RO81QOS:~$ md5sum states.txt
8d7dd71ff51614e69339b03bd1cb86ac  states.txt
dell@DESKTOP-RO81QOS:~$ md5sum states_copy.txt
8d7dd71ff51614e69339b03bd1cb86ac  states_copy.txt
dell@DESKTOP-RO81QOS:~$ shasum states.txt
588e9de7ffa97268b2448927df41760abd3369a9  states.txt
dell@DESKTOP-RO81QOS:~$ shashum states_copy.txt
Command 'shashum' not found, did you mean:
  command 'shasum' from deb perl (5.40.1-7build1)
Try: sudo apt install <deb name>
dell@DESKTOP-RO81QOS:~$ shasum states_copy.txt
588e9de7ffa97268b2448927df41760abd3369a9  states_copy.txt
dell@DESKTOP-RO81QOS:~$ head -n 5 states_copy > states_copy.txtshahum states_copy.txt
head: cannot open 'states_copy' for reading: No such file or directory
dell@DESKTOP-RO81QOS:~$ shasum states_copy.txt
588e9de7ffa97268b2448927df41760abd3369a9  states_copy.txt
dell@DESKTOP-RO81QOS:~$ head -n 5 states_copy.txt > states_copy
.txtshahum states_copy.txt
dell@DESKTOP-RO81QOS:~$ shasum states_copy.txt
588e9de7ffa97268b2448927df41760abd3369a9  states_copy.txt
dell@DESKTOP-RO81QOS:~$ less states_copy.txt
dell@DESKTOP-RO81QOS:~$
dell@DESKTOP-RO81QOS:~$ head - 5 states.txt > states_copy.txt

^C
dell@DESKTOP-RO81QOS:~$ less states_copy.txt
dell@DESKTOP-RO81QOS:~$ shasum states_copy.txt
34313ea9f097bee72a4b071dbdadbc123745dd67  states_copy.txt
dell@DESKTOP-RO81QOS:~$
