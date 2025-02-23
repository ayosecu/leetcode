"""
# Requirements
1.	Read a CSV file containing security logs.
2.	Convert logs to JSON format.
3.	Extract threat indicators from the logs:
    •	IP addresses
    •	File hashes (MD5, SHA256)
    •	URLs
4.	Perform API lookups on VirusTotal for each extracted indicator.
5.	Send alerts via a webhook if a threat is detected.

# VirusTotal Ex    
----------------------
import requests

API_KEY = "your_virustotal_api_key"
file_hash = "d41d8cd98f00b204e9800998ecf8427e"
url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
headers = {"x-apikey": API_KEY}

response = requests.get(url, headers=headers)
print(response.json())
----------------------

# Webhook Ex
----------------------
import json

webhook_url = "https://security-alert-webhook.com"
alert_data = {"alert": "Malicious file detected", "file_hash": file_hash}

requests.post(webhook_url, data=json.dumps(alert_data), headers={"Content-Type": "application/json"})
----------------------
"""
import csv, json, requests

def readCSV(filename):
    f = open(filename, "r")
    reader = csv.DictReader(f)

    dic_list = []
    for line in reader:
        dic_list.append(line)

    return dic_list

def extractIndicators(dic_list):
    dic = { "ips": set(), "hashes": set(), "urls": set() }

    for line in dic_list:
        dic["ips"].add(line["source_ip"])
        dic["ips"].add(line["destination_ip"])
        dic["hashes"].add(line["file_hash"])
        dic["urls"].add(line["url"])
    
    return dic

def checkVT(val):   
    API_KEY = ""
    HEADER = { "x-apikey": API_KEY }
    response = requests.get(f"https://www.virustotal.com/api/v3/files/{val}", headers=HEADER)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print("Response Error")

    return None

def sendAlert(file_hash):
    webhook_url = "https://security-alert-webhook.com"
    alert_data = { "alert": "Malicious file detected", "file_hash": file_hash }
    requests.post(webhook_url, data=json.dumps(alert_data), headers={"Content-Type": "application/json"})


dic_list = readCSV("hash.csv")
indicators = extractIndicators(dic_list)

for key, vals in indicators.items():
    if type == "hashes":
        for val in vals:
            response = checkVT(val)
            if response:
                sendAlert(val)
