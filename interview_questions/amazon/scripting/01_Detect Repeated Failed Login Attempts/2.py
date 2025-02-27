"""
- Problem Statement: Write a Python script that reads a log file (auth.log) and detects IP addresses with more than 5 failed login attempts.
- Input:
Feb 10 10:30:12 server sshd[12345]: Failed password for root from 192.168.1.100 port 22 ssh2
Feb 10 10:32:05 server sshd[12345]: Failed password for invalid user admin from 192.168.1.101 port 22 ssh2
Feb 10 10:35:22 server sshd[12345]: Failed password for root from 192.168.1.100 port 22 ssh2
Feb 10 10:35:25 server sshd[12345]: Failed password for root from 192.168.1.100 port 22 ssh2
Feb 10 10:35:25 server sshd[12345]: Success for root from 192.168.1.100 port 22 ssh2
Feb 10 10:35:32 server sshd[12345]: Failed password for root from 192.168.1.100 port 22 ssh2
Feb 10 10:35:42 server sshd[12345]: Failed password for root from 192.168.1.100 port 22 ssh2
Feb 10 10:35:59 server sshd[12345]: Failed password for root from 192.168.1.100 port 22 ssh2

- Expected Output:
    Suspicious IPs:
    192.168.1.100 (6 failed attempts)
"""
import re
from collections import defaultdict

def findFailedLogin(log_file):
    f = open(log_file, "r")
    lines = f.readlines()

    dic = defaultdict(int)
    for l in lines:
        match = re.search(r"Failed password.*from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", l)
        if match:
            ip = match.group(1)
            dic[ip] += 1
    
    print("Suspicious IPs:")
    for key, val in dic.items():
        if val > 5:
            print(f"{key} ({val} failed attempts)")

findFailedLogin("auth.log")