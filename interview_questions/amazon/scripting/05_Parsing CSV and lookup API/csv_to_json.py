import csv, json

def csvToJson(csv_file, json_file):
    cf = open(csv_file, "r")
    csv_file = csv.DictReader(cf)

    dic_list = []
    for line in csv_file:
        dic_list.append(line)
    
    jf = open(json_file, "w")
    jf.write(json.dumps(dic_list, indent=4))
  
csvToJson("hash.csv", "out.json")