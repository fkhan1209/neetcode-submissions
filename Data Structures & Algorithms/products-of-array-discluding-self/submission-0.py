class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Two pass solution
        # Need to track "prefix" and "postfix" for each element
        # Prefix: product of values up to the specific element 
        # Postfix: product of values after specific element in array
        res = [1] * len(nums)
        pre = 1
        for i in range (len(nums)): 
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range (len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res