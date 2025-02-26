"""
- Problem Statement:
Write a Python script that converts a JSON log file to CSV format. Each JSON object represents a security event.

# input.json
[
  {"event_time": "2024-02-04T12:34:56Z", "username": "alice", "source_ip": "192.168.1.10", "action": "failed_login"},
  {"event_time": "2024-02-04T13:10:22Z", "username": "bob", "source_ip": "203.0.113.20", "action": "successful_login"}
]

# output.csv
event_time,username,source_ip,action
2024-02-04T12:34:56Z,alice,192.168.1.10,failed_login
2024-02-04T13:10:22Z,bob,203.0.113.20,successful_login
"""
import json, csv

def convertJSONtoCSV(jfile, cfile):
    jf = open(jfile,"r")
    data = json.load(jf)
    header = data[0].keys()

    cf = open(cfile, "w")
    writer = csv.DictWriter(cf, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)

convertJSONtoCSV("input.json", "output.csv")
