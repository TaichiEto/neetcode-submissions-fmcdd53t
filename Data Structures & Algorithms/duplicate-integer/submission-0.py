class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        for i in nums:
            if i in uniques:
                return True
                break
            else:
                uniques.add(i)
        return False
