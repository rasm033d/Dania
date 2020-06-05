import os
from pathlib import Path
import random
from shutil import copy
import time
log = open("log.txt", "a") 
path = r"\\192.168.0.112\Anonymous\SlowStorage\Testthings\Windows.iso"
output = r"C:\Users\Rasmus D. Hansen\Documents\test"
count = 0
while count < 100:
    StartTime = time.time()
    copy(path, output)
    endTime = time.time() - StartTime
    print(endTime)
    log.write("\n")
    log.write(str(endTime))
    count = count + 1
