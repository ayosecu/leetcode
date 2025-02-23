class Solution:
    def reformat(self, s: str) -> str:
        # no two adjacent characters have the same type
        # return empty string if it impossible to reformat the string

        letter_st = []
        digit_st = []

        for c in s:
            if c.isalpha():
                letter_st.append(c)
            elif c.isdigit():
                digit_st.append(c)
        
        if abs(len(letter_st) - len(digit_st)) > 1:
            return ""

        if len(letter_st) < len(digit_st):
            letter_st, digit_st = digit_st, letter_st
        
        result = []
        for _ in range(len(digit_st)):
            result.append(letter_st.pop())
            result.append(digit_st.pop())

        if letter_st:
            result.append(letter_st.pop())
        
        return "".join(result)