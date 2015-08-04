#!/usr/bin/env python

from subprocess import PIPE, Popen
import re

x = Popen(['ssh', 'centos-client', 'ip', 'route', 'show'], stdout=PIPE)

r_match = re.compile(r"169\.254|default")

f = open("output.txt", "w")

for line in x.stdout:
    if not r_match.search(line):
        subnet = '192.168.1.100/30' #line.split()[0]
        scan_report = Popen([ 'nmap', '-R', '-sP', '-oG', '-', subnet ], stdout=PIPE).stdout
        for line in scan_report:
            if '#' not in line:
                #ip, hostname, status = line.split()[1], line.split()[2], line.split()[4]
                s = line.split()[1], line.split()[2], line.split()[4]
                f.write(",".join(s) + "\n")
f.close()
