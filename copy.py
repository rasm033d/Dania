import os
from pathlib import Path
import random
from shutil import copy
import time 
path = r"<input path>"
output = r"<output path>"
count = 0
log = open("<path to log file>", "a")
while count < 100:
    StartTime = time.time() #starts time
    files = os.listdir(path) #list of all files in directory
    index = random.randrange(0, len(files)) #takes a random file from said directory
    file = files[index] #sets a variual to a random file
    filepath = os.path.join(path,file) #creates a useable OS path to the file
    print(files[index]) #prints which file was picked
    copy(filepath, output) #copies the file to the output folder
    endTime = time.time() - StartTime #measures the time it takes for said copy to happen
    print(endTime) #prints the time
    log.write(str(files[index]))
    log.write(str(endTime))
    count = count + 1 #increments the count
