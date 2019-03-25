# sudo apt install p7zip-full -y
import os
import sys
from time import time
from multiprocessing import Process, Pool, Value

def start_time():
    start_time = time()
    print("Start!")
    return start_time

def end_time(my_started_time):
    print("%s seconds " % (str(time()-my_started_time)))

def check_argv():
    if len(sys.argv) == 3:
        return True
    else:
        print("Usage : ")
        print("7z_cracker.py [Password Dictionary] [Encrypted 7z File]")
        exit(1)

def crack(line):
    global try_number
    global FINISH
    global my_pass

    with FINISH.get_lock():
        if FINISH.value is 0:
            x = os.system("7z x {} -p{} -bsp0 -bso0 -bse0 -y".format(sys.argv[2], line))
        
            with try_number.get_lock():
                try_number.value = try_number.value + 1
            print("Tried " + str(try_number.value) + " times. => " + line)
    
            if x == 0:
                FINISH.value = True
                my_pass = line
                print("=========================")
                print("\nPassword is : " + my_pass)
                print("=========================")
                end_time(my_started_time)    
        

def multi_crack():
    f = open(sys.argv[1],"r")
    lines = f.read().splitlines()

    global try_number
    global FINISH
    try_number = Value('i', 0)
    FINISH = Value('b', False)

    pool = Pool(processes=4)
    pool.map(crack, lines)
    pool.terminate()
    pool.join()

try_number = 0
FINISH = False
my_pass = ''

if __name__ == "__main__":
    try_number = 0
    if check_argv() == True:
        my_started_time = start_time()
        multi_crack()
