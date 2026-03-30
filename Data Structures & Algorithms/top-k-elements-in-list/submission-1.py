class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            # 1. getの引数を修正
            count[num] = count.get(num, 0) + 1
            
        # 2. reverse=True で多い順にソート
        count_sorted = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        # 3. ソート済みリスト(count_sorted)から先頭k個の「キー(x[0])」を取り出す
        ans = []
        for i in range(k):
            ans.append(count_sorted[i][0])
            
        return ans