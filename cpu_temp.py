#!/usr/bin/python
# -*- coding: utf-8 -*- 

import subprocess
from time import sleep

def cpu_temp():
    """Read and return Raspberry Pi's CPU temperature."""
    output = subprocess.check_output(["vcgencmd", "measure_temp"])
    return output[:-1]


if __name__ == '__main__':
    while True:
        print cpu_temp()
        sleep(2)