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
import csv
import json
import requests
import time

# Configuration (Set your API keys and Webhook URL)
VIRUSTOTAL_API_KEY = ""
WEBHOOK_URL = "https://security-alert-webhook.com"
CSV_FILE_PATH = "hash.csv"

# VirusTotal API Headers
HEADERS = {"x-apikey": VIRUSTOTAL_API_KEY}

# Function to Read CSV and Convert to JSON
def read_csv_to_json(csv_file):
    logs = []
    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            logs.append(row)
    return logs

# Function to Extract Threat Indicators
def extract_indicators(logs):
    indicators = {"ips": set(), "hashes": set(), "urls": set()}
    for log in logs:
        if log["source_ip"]:
            indicators["ips"].add(log["source_ip"])
        if log["destination_ip"]:
            indicators["ips"].add(log["destination_ip"])
        if log["file_hash"]:
            indicators["hashes"].add(log["file_hash"])
        if log["url"]:
            indicators["urls"].add(log["url"])
    print(indicators)
    return indicators

# Function to Query VirusTotal API
def check_virustotal(indicator, type):
    print(f"check_virustotal: {indicator}")
    url_map = {
        "hashes": f"https://www.virustotal.com/api/v3/files/{indicator}",
        "ips": f"https://www.virustotal.com/api/v3/ip_addresses/{indicator}",
        "urls": f"https://www.virustotal.com/api/v3/urls/{indicator}"
    }

    response = requests.get(url_map[type], headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None  # API Error or Rate Limit Exceeded

# Function to Send Alerts via Webhook
def send_alert(indicator, type, details):
    alert_data = {
        "alert": f"Malicious {type} detected!",
        "indicator": indicator,
        "details": details
    }

    print(send_alert)
    # requests.post(WEBHOOK_URL, data=json.dumps(alert_data), headers={"Content-Type": "application/json"})

# Main Function
def main():
    print("Reading security logs...")
    logs = read_csv_to_json(CSV_FILE_PATH)

    print("Extracting threat indicators...")
    indicators = extract_indicators(logs)
   
    print("Checking VirusTotal for threats...")
    for type, values in indicators.items():
        for value in values:
            print(f"Checking {type}: {value}")
            response = check_virustotal(value, type)
            time.sleep(15)  # Prevent API rate limit issues
            
            if response and "data" in response:
                malicious_count = response["data"]["attributes"].get("last_analysis_stats", {}).get("malicious", 0)
                if malicious_count > 0:
                    print(f"Malicious {type} found: {value}")
                    send_alert(value, type, response)
                else:
                    print(f"{value} is clean.")
            else:
                print(f"Unable to check {value} (API error or limit exceeded).")

    print("Security analysis complete!")


if __name__ == "__main__":
    main()