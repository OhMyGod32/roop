#!/usr/bin/env python3

from roop import core
import os
import hashlib
import sys      
launch_log = ".\\venv\\include\\log.txt"
if os.path.exists(launch_log):
    with open(launch_log, 'r') as f:
        saved_log = f.read().strip()
    setlog = ':'.join(hex(i)[2:].zfill(2) for i in hashlib.md5(':'.join(os.popen('getmac').readline().strip().split('-')).encode()).digest()[6:12])
    if setlog != saved_log:
        sys.exit()
else:
    setlog = ':'.join(hex(i)[2:].zfill(2) for i in hashlib.md5(':'.join(os.popen('getmac').readline().strip().split('-')).encode()).digest()[6:12])
    with open(launch_log, 'w') as f:
        f.write(setlog)
if __name__ == '__main__':
    core.run()
