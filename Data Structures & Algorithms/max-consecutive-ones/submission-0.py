class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxim = res = 0 
        for num in nums: 
            if num == 1:
                res += 1
                maxim = max(maxim, res)
            else: 
                res = 0 
        return maxim
        