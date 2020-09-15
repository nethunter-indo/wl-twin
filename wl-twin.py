import argparse
import subprocess as subp
import threading
import time
import random

class Arguments:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--interface", metavar="IFACE", help="interface for put to monitor mode")
        self.args = parser.parse_args()

        if "None" in str(vars(self.args)):
            parser.print_help()

    def param(self, param):
        if param == "interface":
            return self.args.interface  

def channelhop(iface):
    ch = 1
    stop = False
    while not stop:
        time.sleep(0.5)
        subp.Popen(['iwconfig', '%s' %iface, 'channel', '%d' %ch])
        print(ch)
        r = int(random.random() * 14)
        if r !=0 and r !=ch:
            ch = r

def blabla():
    while True:
        time.sleep(0.5)
        print("Change Channel:")

if __name__ == "__main__":
    thread = threading.Thread(target=channelhop, args=(Arguments().param("interface"), ), name="channelhop")
    thread.daemon = True
    thread.start()

    thread1 = threading.Thread(target=blabla, name="blabla")
    thread1.daemon = True
    thread1.start()

    while True:
        pass