import random

class RandomizedSet(object):

    def __init__(self):
        self.random_map = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.random_map:
            self.random_map.add(val)
            return True
        else:
            return False
    
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.random_map:
            return False
        else:
            self.random_map.remove(val)
            return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.random_map)) # list conversion makes O(n) so need to be fixed
        

def main():
    # Your RandomizedSet object will be instantiated and called as such:
    obj = RandomizedSet()
    param_1 = obj.insert(1)
    param_2 = obj.remove(2)
    param_3 = obj.getRandom()
    print(param_1, param_2, param_3)
    
if (__name__) == "__main__":
    main()