# sudo apt install p7zip-full -y
# need "rockyou.txt" file
# iconv -c -f euc-kr -t utf-8 rockyou.txt > rockyou_utf8.txt

import os
import sys

def check_argv():
    if len(sys.argv) == 3:
        return True
    else:
        print("Usage : ")
        print("7z_Cracker.py [Password Dictionary] [Encrypted 7z File]")
        exit(1)


def crack():
    f = open(sys.argv[1],'r')
    lines = f.read().splitlines()
    try_number = 0
    for line in lines:
        try_number = try_number + 1
        x = os.system("7z x {} -p{} -bsp0 -bso0 -bse0 -y".format(sys.argv[2], line))
        print("Tried "+ str(try_number) + " times. => " + line)
    #     print("x = " + str(x))
    #     https://stackoverflow.com/questions/6466711/what-is-the-return-value-of-os-system-in-python
        if x == 0:
            print("====================================")
            print("Password is : " + line)
            print("====================================")
            exit(1)
    print("Couldn't found password...")

if __name__ == '__main__':
    if check_argv() == True:
        crack()