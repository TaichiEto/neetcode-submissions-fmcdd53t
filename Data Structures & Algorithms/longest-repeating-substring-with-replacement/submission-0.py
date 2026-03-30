class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_count = 0
        ans = 0 # ansいる？
        for right in range(len(s)):
            # 1. 右の文字をcountに追加し、max_countを更新する。
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])
            # 2. 窓の中の「書き換えるべき文字数」がkを超えたら
            # (窓の長さ - 一番多い文字の数 > k)
            if (right - left + 1) - max_count > k:
                # 左端の文字を捨てて、leftを進める
                count[s[left]] = count.get(s[left], 0) - 1
                left += 1
            
            # 3. 最大の窓の長さを記録する
            ans = max(ans, right - left + 1)
        
        return ans