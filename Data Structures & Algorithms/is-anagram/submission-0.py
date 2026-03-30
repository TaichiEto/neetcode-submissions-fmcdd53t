class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if number of chars is different, the answer is false.
        if len(s) != len(t):
            return False
        
        count_S = {}
        count_T = {}

        for i in range(len(s)):
            count_S[s[i]] = count_S.get(s[i], 0) + 1
            count_T[t[i]] = count_T.get(t[i], 0) + 1
        
        return count_S == count_T