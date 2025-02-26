"""
- Extract Failed SSH Logins from AWS Logs
- Task: Given CloudTrail logs, extract failed SSH login attempts.

# Input Example (CloudTrail JSON Log Entry)
{
  "eventTime": "2024-02-04T12:34:56Z",
  "eventName": "ConsoleLogin",
  "userIdentity": {"type": "IAMUser", "userName": "alice"},
  "sourceIPAddress": "192.168.1.10",
  "errorMessage": "Failed authentication"
}

# Expect Output
User: alice, IP: 192.168.1.10, Time: 2024-02-04T12:34:56Z
"""
import json

def extractInfo(log):
    j_log = json.loads(log)

    if "errorMessage" in j_log:
        print(f"User: {j_log["userIdentity"]["userName"]}, IP: {j_log["sourceIPAddress"]}, Time: {j_log["eventTime"]}")

def extractInfoFile(filename):
    jf = open(filename, "r")
    j_log = json.load(jf)

    for log in j_log:
        if "Fail" in log["errorMessage"]:
                print(f"User: {log["userIdentity"]["userName"]}, IP: {log["sourceIPAddress"]}, Time: {log["eventTime"]}")

log = '''
{
  "eventTime": "2024-02-04T12:34:56Z",
  "eventName": "ConsoleLogin",
  "userIdentity": {"type": "IAMUser", "userName": "alice"},
  "sourceIPAddress": "192.168.1.10",
  "errorMessage": "Failed authentication"
}
'''

extractInfo(log)
extractInfoFile("log.json")