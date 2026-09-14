dell@DESKTOP-RO81QOS:~$ egrep "[aeiou]" small.txt
 hey
abcdefghijklmnopqrstuvwxyz
aa bb cc
abc
tragedy + time = humor
http://www.jhsph.edu/
abcdefghijklmnopqrstuvwxyz
aa bb cc
abc
tragedy + time = humor
http://www.jhsph.edu/
dell@DESKTOP-RO81QOS:~$ egrep "[^aeiou]" small.txt
 hey
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
aa bb cc
rhythms
xyz
abc
tragedy + time = humor
http://www.jhsph.edu/
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
aa bb cc
rhythms
xyz
abc
tragedy + time = humor
http://www.jhsph.edu/
#%&-=***=-&%#
dell@DESKTOP-RO81QOS:~$ egrep "[^aeiouAEIOU]" small.txt
 hey
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
aa bb cc
rhythms
xyz
abc
tragedy + time = humor
http://www.jhsph.edu/
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
aa bb cc
rhythms
xyz
abc
tragedy + time = humor
http://www.jhsph.edu/
#%&-=***=-&%#
dell@DESKTOP-RO81QOS:~$ egrep "[e-q]" small.txt
 hey
abcdefghijklmnopqrstuvwxyz
rhythms
tragedy + time = humor
http://www.jhsph.edu/
abcdefghijklmnopqrstuvwxyz
rhythms
tragedy + time = humor
http://www.jhsph.edu/
dell@DESKTOP-RO81QOS:~$ egrep "[E-Q]" small.txt
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXYZ
dell@DESKTOP-RO81QOS:~$ egrep "[E-Qe-q]" small.txt
 hey
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
rhythms
tragedy + time = humor
http://www.jhsph.edu/
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
rhythms
tragedy + time = humor
http://www.jhsph.edu/
dell@DESKTOP-RO81QOS:~$ egrep '\." small.txt
> ^C
dell@DESKTOP-RO81QOS:~$ egrep '\+' small.txt
tragedy + time = humor
tragedy + time = humor
dell@DESKTOP-RO81QOS:~$ egrep '\.' small.txt
http://www.jhsph.edu/
http://www.jhsph.edu/
dell@DESKTOP-RO81QOS:~$ egrep "(iss){2}" states.txt
Mississippi
dell@DESKTOP-RO81QOS:~$ egrep "s{2,3}" states.txt
Massachusetts
Mississippi
Missouri
Tennessee
dell@DESKTOP-RO81QOS:~$ egrep "\+" small.txt
tragedy + time = humor
tragedy + time = humor
dell@DESKTOP-RO81QOS:~$ egrep "^M" small.txt
dell@DESKTOP-RO81QOS:~$ egrep "^M" states.txt
Maine
Maryland
Massachusetts
Michigan
Minnesota
Mississippi
Missouri
Montana
dell@DESKTOP-RO81QOS:~$ egrep "$a" states.txt
Alabama
Alaska
Arizona
Arkansas
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
Iowa
Kansas
Kentucky
Louisiana
Maine
Maryland
Massachusetts
Michigan
Minnesota
Mississippi
Missouri
Montana
Nebraska
Nevada
New Hampshire
New Jersey
New Mexico
New York
North Carolina
North Dakota
Ohio
Oklahoma
Oregon
Pennsylvania
Rhode Island
South Carolina
South Dakota
Tennessee
Texas
Utah
Vermont
Virginia
Washington
West Virginia
Wisconsin
Wyoming
dell@DESKTOP-RO81QOS:~$ egrep "*a" states.txt
grep: warning: * at start of expression
Alabama
Alaska
Arizona
Arkansas
California
Colorado
Delaware
Florida
Georgia
Hawaii
Idaho
Indiana
Iowa
Kansas
Louisiana
Maine
Maryland
Massachusetts
Michigan
Minnesota
Montana
Nebraska
Nevada
New Hampshire
North Carolina
North Dakota
Oklahoma
Pennsylvania
Rhode Island
South Carolina
South Dakota
Texas
Utah
Virginia
Washington
West Virginia
dell@DESKTOP-RO81QOS:~$ egrep "north|south states.txt
> ^C
dell@DESKTOP-RO81QOS:~$ egrep "north|south" states.txt
dell@DESKTOP-RO81QOS:~$ egrep "North|South" states.txt
North Carolina
North Dakota
South Carolina
South Dakota
dell@DESKTOP-RO81QOS:~$ egrep "t$" states.txt
Connecticut
Vermont
dell@DESKTOP-RO81QOS:~$ egrep -n "t$" states.txt
7:Connecticut
45:Vermont
dell@DESKTOP-RO81QOS:~$ egrep "New" states.txt small.txt
states.txt:New Hampshire
states.txt:New Jersey
states.txt:New Mexico
states.txt:New York
dell@DESKTOP-RO81QOS:~$ egrep "^[AEIOU]{1}.+[aeiou]{1}$" states.txt
Alabama
Alaska
Arizona
Idaho
Indiana
Iowa
Ohio
Oklahoma
dell@DESKTOP-RO81QOS:~$ egrep "^[AEIOU].+[aeiou]$" states.txt
Alabama
Alaska
Arizona
Idaho
Indiana
Iowa
Ohio
Oklahoma
dell@DESKTOP-RO81QOS:~$ egrep "^[AEIOU]+[aeiou]$" states.txt
dell@DESKTOP-RO81QOS:~$
