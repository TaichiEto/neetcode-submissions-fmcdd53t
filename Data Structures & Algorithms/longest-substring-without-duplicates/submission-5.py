class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        if len(s) == 1:
            return 1
        for left in range(len(s)):
            window_content = set()
            right = left
            while right < len(s) and s[right] not in window_content:
                window_content.add(s[right])
                right+=1
            ans = max(ans, (right - left))
        return ans