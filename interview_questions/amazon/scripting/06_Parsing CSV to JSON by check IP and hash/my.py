"""
You are given a CSV file containing security logs with details about network events. Your task is to:
	1.	Read the CSV file and convert each log entry into JSON format.
	2.	Extract file hashes and IP addresses from the logs.
	3.	Perform simple validation checks on the extracted data.
	•	A valid IP address follows the x.x.x.x format (e.g., 192.168.1.1).
	•	A valid MD5 file hash is a 32-character hexadecimal string.
	4.	Return the processed logs in JSON format.

# input.csv
timestamp,source_ip,destination_ip,file_hash,event_type
2024-02-01T12:34:56Z,192.168.1.100,8.8.8.8,d41d8cd98f00b204e9800998ecf8427e,malware_detected
2024-02-01T12:35:10Z,invalid_ip,8.8.4.4,not_a_hash,failed_login


# return
{
    "timestamp":"2024-02-01T12:34:56Z",
    "source_ip":"192.168.1.100",
    "destination_ip":"8.8.8.8",
    "file_hash":"d41d8cd98f00b204e9800998ecf8427e",
    "event_type":"malware_detected",
    "valid_ip":True,
    "valid_hash":True
}

"""
import csv, re, json

def checkHash(hash):
    return bool(re.match(r"^[a-fA-F0-9]{32}$", hash))


def checkIP(ip):
    return bool(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip))

def readCSV(filename):
    f = open(filename, "r")
    reader = csv.DictReader(f)

    result = []
    for row in reader:
        row["valid_ip"] = checkIP(row["source_ip"])
        row["valid_hash"] = checkHash(row["file_hash"])
        result.append(row)
        
    return result

def convertJSON(content):
    return json.dumps(content, indent=4)


content = readCSV("input.csv")
print(convertJSON(content))
