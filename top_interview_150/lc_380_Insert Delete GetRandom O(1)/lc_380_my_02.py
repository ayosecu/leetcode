import random

"""
    - Time Complexity: O(1) for each function.
    - Space Complexity: O(n), n = the number of vals (insert calls).
"""
class RandomizedSet:
    def __init__(self):
        # Use Dictionary (val:index) and list (vals)
        self.dic_vals = {}
        self.list_vals = []

    def insert(self, val: int) -> bool:
        if val not in self.dic_vals:
            idx = len(self.list_vals)
            self.dic_vals[val] = idx
            self.list_vals.append(val)
            return True
        else:
            return False        

    def remove(self, val: int) -> bool:
        if val not in self.dic_vals:
            return False
        else:
            # copy last val of list to val's index and change the index
            idx = self.dic_vals[val]
            self.list_vals[idx] = self.list_vals[-1]
            self.dic_vals[self.list_vals[-1]] = idx
            # remove the last item of vals list
            self.list_vals.pop()
            # delete val from dictionary
            del self.dic_vals[val]            
            return True
        
    def getRandom(self) -> int:
        return random.choice(self.list_vals)
        

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.getRandom()
print(param_1, param_2, param_3)