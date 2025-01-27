def main(ransomNote, magazine):
    m_dic = {}
    r_dic = {}

    for ch in magazine:
        if ch in m_dic:
            m_dic[ch] += 1
        else:
            m_dic[ch] = 1

    for ch in ransomNote:
        if ch in r_dic:
            r_dic[ch] += 1
        else:
            r_dic[ch] = 1
    
    for key in r_dic:
        if key not in m_dic:
            return False
        
        if r_dic[key] > m_dic[key]:
            return False
    
    return True

if (__name__)==("__main__"):
    tc = [
            ["a", "b"],
            ["aa", "ab"],
            ["aa", "aab"]
    ]

    for t in tc:
        print(main(t[0], t[1]))
