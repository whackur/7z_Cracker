# sudo apt install p7zip-full -y
import os
import sys
from time import time
from multiprocessing import Process, Pool

def start_time():
    start_time = time()
    print("Start!")
    return start_time

def end_time(my_started_time):
    print("%s seconds " % (str(time() - my_started_time)))
    exit(1)

def check_argv():
    if len(sys.argv) == 3:
        return True
    else:
        print("Usage : ")
        print("7z_cracker.py [Password Dictionary] [Encrypted 7z File]")
        exit(1)


def crack(lines):
    global try_number
    try_number = try_number + 1
    x = os.system("7z x {} -p{} -bsp0 -bso0 -bse0 -y".format(sys.argv[2], lines))
    print("Tried "+ str(try_number) + " times. => " + lines)

    if x == 0:
        print("====================================")
        print("Password is : " + lines)
        print("====================================")
        

def multi_crack():
    f = open(sys.argv[1],'r')
    lines = f.read().splitlines()
    pool = Pool(processes=4)
    pool.map(crack, lines)
    pool.close()
    pool.join()

    end_time(my_started_time)

if __name__ == '__main__':
    try_number = 0
    my_started_time = start_time()
    if check_argv() == True:
        multi_crack()
