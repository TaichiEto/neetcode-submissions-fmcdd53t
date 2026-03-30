class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        
        # ステップ1: 左側だけの累計（前の結果を引き継ぐ！）
        prefix = [1] * n
        for i in range(1, n):
            # 「1つ前の左累計」 × 「1つ左の数字」＝ 今の左累計
            prefix[i] = prefix[i-1] * nums[i-1] 
            
        # ステップ2: 右側だけの累計（前の結果を引き継ぐ！）
        postfix = [1] * n
        for i in range(n - 2, -1, -1): # -1まで回して 0 を含める
            # 「1つ前の右累計」 × 「1つ右の数字」＝ 今の右累計
            postfix[i] = postfix[i+1] * nums[i+1]
            
        # ステップ3: 右と左をくっつける
        for i in range(n):
            ans.append(prefix[i] * postfix[i])
            
        return ans