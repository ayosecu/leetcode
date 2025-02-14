"""
- Problem Statement
You are given two separate log files containing different types of events related to system activity. Your task is to correlate related events from both logs based on a common identifier (e.g., IP address, session ID, or transaction ID). You should efficiently store the parsed data using a hash map of lists, allowing O(1) lookup time for future queries.

- Input Description
You will receive two log files in text format:
	1.	Log File 1 (log1.txt) : [Timestamp] [TransactionID] Event1 details...
    2.	Log File 2 (log2.txt) : [Timestamp] [TransactionID] Event2 details...

- Requirements
1. Parse the logs and store data in a hash map of lists, where:
 • The key is the TransactionID.
 • The value is a list of log events associated with that transaction.
2. Ensure O(1) lookup time for any given TransactionID.
3. Print all correlated events for a given TransactionID.
4. Handle edge cases:
 • Logs may contain unrelated transaction IDs.
 • Logs may not be sorted by time.
 • Some transaction IDs may only appear in one log.

- Expected Output
Transaction ID: TXN123
[2025-02-12 10:15:23] Failed login attempt from 192.168.1.1
[2025-02-12 10:15:25] IP 192.168.1.1 was blocked by firewall

- Constraints
 • Each log file contains at most 10⁶ entries.
 • Each log line has a maximum length of 256 characters.
 • The number of unique TransactionIDs does not exceed 10⁵.
"""
import re
from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.dic_index = defaultdict(list)
        return
    
    def parseLog(self, logFileName):
        f = open(logFileName, "r")
        lines = f.readlines()

        for line in lines:
            parsed = re.search(r"\[(.*)\] (\S+) (.*)", line)
            time = parsed.group(1)
            id = parsed.group(2)
            log = parsed.group(3)
            self.dic_index[id].append((time, log))

        return
    
    def query(self, key):
        print(f"Transaction ID: {key}")               
        if key in self.dic_index:
            for time, log in self.dic_index[key]:
                print(f"[{time}] {log}")
        else:
            print("--- No Result ---")

        return

files = ["log1.txt", "log2.txt"]

sol = Solution()
for file in files:
    sol.parseLog(file)
sol.query("TXN123")