# Runs on Leetcode
    # Runtime - O(nlogn)
    # space - O(1)
class Solution(object):
    def arrayPairSum(self, nums):
        if not nums:
            return
        nums.sort()
        n=0
        for i in range(0,len(nums),2):
            n+=min(nums[i],nums[i+1])
        # print(n)
        return n
            