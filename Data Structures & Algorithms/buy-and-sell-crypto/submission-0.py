class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for left in range(len(prices)):
            for right in range(left+1,len(prices)):
                tmp = prices[right] - prices[left]
                if tmp > profit:
                    profit = tmp
        return profit