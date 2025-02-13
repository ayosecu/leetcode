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

"""
    - Is this a log file name fixed?
        - fixed
    - criteria (5) fixed?
        -> parameter
    - can assume pattern is "Failed password xxxx from IP" ?
        -> regex
    - ip is only ipv4? or ipv6 can be?
        -> ipv4 only
"""
import sys
import re
from collections import defaultdict

def checkFailedUser(criteria):
    file_name = "auth.log"
    try:
        # File Open    
        file = open(file_name, "r")
    except FileNotFoundError:
        print(f"Error - {file_name} file not found!!")
        sys.exit(1)
    
    dict_fail_count = defaultdict(int)

    for line in file.readlines():
        # check pattern (regix)
        match = re.search(r"Failed.*from (\d+\.\d+\.\d+\.\d+)", line)

        if match:
            # extract IP
            ip = match.group(1)
            # update count via dictionary
            dict_fail_count[ip] += 1
   
    # print result
    count_result = 0
    for ip, count in dict_fail_count.items():
        if count > criteria:
            if not count_result:
                print("Suspicious IPs:")
            print(f"\t{ip} ({count} failed attempts)")
            count_result += 1

checkFailedUser(5)