class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                elif sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
    
                    left += 1
                    right -= 1
                    
                    # 進めた先が「さっきと同じ値」なら、違う値が出るまでスキップ
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return ans