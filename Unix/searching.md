dell@DESKTOP-RO81QOS:~$ cd
dell@DESKTOP-RO81QOS:~$ pwd
/home/dell
dell@DESKTOP-RO81QOS:~$ find . -name "states.txt"
./document/states.txt
./states.txt
dell@DESKTOP-RO81QOS:~$ find . -name "*.jpg"
./1612671068880.jpg
./1612671023099.jpg
./1612671046779.jpg
./2024/IMG_20210207_144356.jpg
./2024/IMG_20210208_192900.jpg
./2024/IMG_20210216_135808.jpg
./2024/IMG_20210222_150046.jpg
./2024/IMG_20210212_175537.jpg
./2020/IMG_20200722_092952.jpg
./2020/IMG_20200709_184302.jpg
./2020/IMG_20200722_092924.jpg
./2020/IMG_20200709_184011.jpg
./2020/IMG_20200624_112102.jpg
./1612671068880 (2).jpg
./1612671119937.jpg
dell@DESKTOP-RO81QOS:~$ egrep "*name*" states.txt small.txt
grep: warning: * at start of expression
dell@DESKTOP-RO81QOS:~$ egrep "{^aeiou}" states.txt
dell@DESKTOP-RO81QOS:~$ egrep "New" states.txt
New Hampshire
New Jersey
New Mexico
New York
dell@DESKTOP-RO81QOS:~$ grep "^a" states.txt > no_a.txt
dell@DESKTOP-RO81QOS:~$ ls no_a.txt
no_a.txt
dell@DESKTOP-RO81QOS:~$ less no_a.txt
dell@DESKTOP-RO81QOS:~$ head no_a.txt
dell@DESKTOP-RO81QOS:~$ grep -iv "^a" states.txt > no_a.txt
dell@DESKTOP-RO81QOS:~$ head no_a.txt
California
Colorado
Connecticut
Delaware
Florida
Georgia
Hawaii
Idaho
Illinois
Indiana
dell@DESKTOP-RO81QOS:~$ grep -iv "a" states.txt > no_a.txt
dell@DESKTOP-RO81QOS:~$ head no_a.txt
Connecticut
Illinois
Kentucky
Mississippi
Missouri
New Jersey
New Mexico
New York
Ohio
Oregon
