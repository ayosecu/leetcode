class Solution:
    """
        - Time Complexity: O(1)
            - for loop : 13
            - whil loop : max 4
            - join : roman_list could be a max 4*13 = 52 sized array.
        - Space Complexity: O(1)
            - sym_map : fixed sized list
            - roman_list : max 3 * 4 = 12 sized array. (3333)
    """
    def intToRoman(self, num: int) -> str:
        sym_map = [ (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                    (90, "XC"), (50, "L"), (40, "XL"), (10, "X"),
                    (9, "IX"), (5, "V"), (4, "IV"), (1, "I") ]
        
        roman_list = []
        for (val, sym) in sym_map:
            while num >= val:                
                roman_list.append(sym)
                num -= val

        return "".join(roman_list)                