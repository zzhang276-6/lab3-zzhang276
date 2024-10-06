#!/usr/bin/env python3
# Author ID: zzhang276

import subprocess

def free_space():
    process = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
