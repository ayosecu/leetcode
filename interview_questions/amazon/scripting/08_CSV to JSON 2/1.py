"""
- Convert Security Logs (CSV to JSON)
- Task: Write a Python script to convert CSV security logs to JSON format.

# Input (CSV Security Log):
event_time,username,source_ip,action
2024-02-04T12:34:56Z,alice,192.168.1.10,failed_login
2024-02-04T13:10:22Z,bob,203.0.113.20,successful_login

# Output
[
  {"event_time": "2024-02-04T12:34:56Z", "username": "alice", "source_ip": "192.168.1.10", "action": "failed_login"},
  {"event_time": "2024-02-04T13:10:22Z", "username": "bob", "source_ip": "203.0.113.20", "action": "successful_login"}
]
"""
import csv, json

def convertCSVtoJSON(c_filename, j_filename):
    f = open(c_filename, "r")
    reader = csv.DictReader(f)
    
    c_data = list(reader)
    j_data = json.dumps(c_data, indent=4)

    jf = open(j_filename, "w")
    jf.write(j_data)

convertCSVtoJSON("input.csv", "output.json")