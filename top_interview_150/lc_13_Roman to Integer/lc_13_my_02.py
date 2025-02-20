class Solution:
    def romanToInt_my(self, s: str) -> int:
        sym_map = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        sym_map_2 = { "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900 }

        i, sum = 0, 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in sym_map_2:
                sum += sym_map_2[s[i:i+2]]
                i += 2
            else:
                sum += sym_map[s[i]]
                i += 1
        
        return sum

    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(1)
            - sym_map : 7 size
    """
    def romanToInt(self, s: str) -> int:
        sym_map = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }

        sum = 0
        for i in range(len(s)):
            if i + 1 < len(s) and sym_map[s[i]] < sym_map[s[i + 1]]:
                sum -= sym_map[s[i]]
            else:
                sum += sym_map[s[i]]
         
        return sum