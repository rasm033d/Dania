import os
from pathlib import Path
import random
from shutil import copy
import time 
path = r"\\192.168.0.112\Anonymous\Storage\Testthings"
output = r"C:\Users\Rasmus D. Hansen\Documents\test"
count = 0
while count < 100:
    StartTime = time.time()
    files = os.listdir(path)
    index = random.randrange(0, len(files))
    file = files[index]
    filepath = os.path.join(path,file)
    print(files[index])
    copy(filepath, output)
    endTime = time.time() - StartTime
    print(endTime)
    count = count + 1