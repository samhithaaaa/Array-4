#time complexity:o(n)
#space complexity:o(1)
class Solution(object):
    def nextPermutation(self, nums):
        if not nums:
            return
        i=len(nums)-2
        while(i>=0 and nums[i]>=nums[i+1]):
            i-=1
        if i>=0:
            j=len(nums)-1
            while(j>i and nums[j]<=nums[i]):
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
        i+=1
        temp=nums[i:]
        nums[i:]=temp[::-1]
        return 