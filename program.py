import subprocess
import time
import os
filepath = "<path>"
count = 0
log = open("/mnt/storage/log.txt", "a")
while count < 50:
    startTime = time.time()
    subprocess.call(('xdg-open', filepath)) #opens the file with the default program as specified by the OS
    endTime = startTime - time.time()
    log.write("\n") #newline
    log.write(str(endTime)) #writes the time into a .txt file
    os.system("pkill VLC") #kills the assoicated process, so it can run again
    time.sleep(3) #waits 3 second to ensure that everything is closed