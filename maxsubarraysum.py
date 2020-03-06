#time complexity is o(n)
#space complexity is o(1)
class Solution:
    def maxSubArray(self,nums):
        local =nums[0]
        globall=nums[0]
        for i in range(1,len(nums)):
            local=max(local+nums[i],nums[i])
            globall=max(globall,local)
        return globall
