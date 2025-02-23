class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            columnNumber -= 1
            remain = columnNumber % 26

            result.append(chr(ord("A") + remain))
            
            columnNumber //= 26
            
        return "".join(reversed(result))
