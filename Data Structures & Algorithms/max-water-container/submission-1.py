class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest_amount = 0
        for left in range(len(heights)):
            right = len(heights) - 1
            while left < right:
                height = min(heights[left], heights[right])
                pool_size = height * (right - left)
                largest_amount = max(largest_amount, pool_size)
                right -= 1
        
        return largest_amount