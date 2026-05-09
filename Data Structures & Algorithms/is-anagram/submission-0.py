class Solution:
    def isAnagram(self, s: str, t: str) -> bool:       
        if len(s) != len(t):
            return False
        
        s_count = [0] * 26
        t_count = [0] * 26

        for i in range(len(s)):
            s_char = ord(s[i]) - ord('a')
            s_count[s_char] += 1
            t_char = ord(t[i]) - ord('a')
            t_count[t_char] += 1

        return s_count == t_count