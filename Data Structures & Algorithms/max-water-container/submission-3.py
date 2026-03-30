class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_w = 0
        
        while l < r:
            # 現在の左右の高さ
            h_l, h_r = height[l], height[r]
            
            # 面積 = 底辺(r-l) * 高さ(低い方)
            current_w = (r - l) * (h_l if h_l < h_r else h_r)
            
            if current_w > max_w:
                max_w = current_w
            
            # 背が低い方を動かす
            if h_l < h_r:
                l += 1
            else:
                r -= 1
        return max_w

# テスト用
sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])) # 期待値: 49