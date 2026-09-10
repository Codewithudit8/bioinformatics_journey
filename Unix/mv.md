## Before I organized the photos by year, what command would have listed all of the photos of type .png?

## Before I organized the photos by year, what command would have deleted all of my hiking photos?

## What series of commands would you use in order to put my figures for a data science course and the pictures I took in the lab into their own folders?


dell@DESKTOP-RO81QOS:~$ ls .png*
ls: cannot access '.png*': No such file or directory
dell@DESKTOP-RO81QOS:~$ pwd
/home/dell
dell@DESKTOP-RO81QOS:~$ ls .jpg*
ls: cannot access '.jpg*': No such file or directory
dell@DESKTOP-RO81QOS:~$ ls *.jpg
 1612671023099.jpg   '1612671068880 (2).jpg'   1612671119937.jpg
 1612671046779.jpg   1612671068880.jpg
dell@DESKTOP-RO81QOS:~$ rm *hiking*
rm: cannot remove '*hiking*': No such file or directory
dell@DESKTOP-RO81QOS:~$ touch data lab
dell@DESKTOP-RO81QOS:~$ mkdir data_science lab_picture
dell@DESKTOP-RO81QOS:~$ mv data data_science/
dell@DESKTOP-RO81QOS:~$ mv lab lab_picture/
dell@DESKTOP-RO81QOS:~$ ls data_science
data
dell@DESKTOP-RO81QOS:~$ ls lab_picture
lab
dell@DESKTOP-RO81QOS:~$

