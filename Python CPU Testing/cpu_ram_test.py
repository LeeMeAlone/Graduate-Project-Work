import os
import psutil
import thread
import time

import platform

#Created to stop cpu_work() thread
class CancellationToken:
   def __init__(self):
       self.is_cancelled = False

   def cancel(self):
       self.is_cancelled = True

def get_machine_specs():
        #INTRODUCE THE SYSTEM WITH SPECS
        print("="*20, "System Information", "="*20)
        print("CPU Testing / Python")
        print("[CURRENT SYSTEM]: " + platform.system())
        print("[CURRENT PROCESSOR]: " + platform.processor())
        print("[CURRENT MACHINE]: " + platform.machine())
        print("[CURRENT VERSION]: " + platform.version())
        print("[CURRENT VERSION]: " + str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB")
        print("="*60)

def cpu_work(token):
        print("CPU MONITORING")
        while not token.is_cancelled:
                #Sleep every 5 seconds then print a result
                time.sleep(.5)
                print(":"*50)
                print('The CPU usage is: ', psutil.cpu_percent())
                print('RAM memory % used:', psutil.virtual_memory()[2])


def working(token):
        string = ""
        num = 100000000
        print("WORK HAS STARTED")
        for number in xrange(num):
                string += "HELLO"

        print("WORK HAS ENDED")
        token.cancel()

if __name__ == "__main__":
        get_machine_specs()

        #create token
        token = CancellationToken()
 


        # Create two threads for each job
        try:
                thread.start_new_thread(cpu_work, (token, ))
                thread.start_new_thread(working, (token, ))
        except:
           print "Error: unable to start thread"

        while 1:
                pass

