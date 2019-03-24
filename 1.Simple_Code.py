# sudo apt install p7zip-full -y
# need "rockyou.txt" file
# iconv -c -f euc-kr -t utf-8 rockyou.txt > rockyou_utf8.txt

import os

f = open('wordlist.txt','r')
lines = f.read().splitlines()

for line in lines:
    x = os.system("7z x a.simple.7z -p{} -bsp0 -bso0 -bse0 -y".format(line))
#     print("x = " + str(x))
#     https://stackoverflow.com/questions/6466711/what-is-the-return-value-of-os-system-in-python
    if x == 0:
        print("\nPassword is : " + line)
        exit(1)
print("Couldn't found password...")
