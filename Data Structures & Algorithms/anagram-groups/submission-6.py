import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = collections.defaultdict(list)
        for s in strs:
            key = [0] * 100
            for index in range(len(s)):
                char = s[index]
                o = ord(char) - ord('a')
                key[o] += 1
            answer[tuple(key)].append(s)
        return list(answer.values())