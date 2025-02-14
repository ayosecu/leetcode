from collections import defaultdict
import re

class Solution(object):
    def __init__(self):
        self.dict_list = defaultdict(list)

    def parseLogFile(self, fileName):
        try:
            # open file
            f = open(fileName, "r")    
        except:
            print(f"[ERROR] File Open Error: {fileName}")
            return
        
        # read lines
        for line in f.readlines():
            # extract fields by regex    
            match = re.search(r"\[(.*)\] (\S+) (.*)", line)

            # if matched, save fields to list dictionary
            if match:
                time = match.group(1)
                id = match.group(2)
                detail = match.group(3)           
                self.dict_list[id].append(f"[{time}] {detail}")
                
    def query(self, id):
        print(f"Transaction ID: {id}")        
        
        # check key in dictionary
        if id in self.dict_list:
            # sort
            self.dict_list[id].sort()
            # print result                        
            for log in self.dict_list[id]:
                print(log)
        else:
            print("--- No Result ---")
        return

sol = Solution()
sol.parseLogFile("log1.txt")
sol.parseLogFile("log2.txt")
sol.query("TXN123")
sol.query("TXN321")