class Solution(object):
    def averageValue(self, nums):
        sum=0
        count=0
        for i in range(0,len(nums)):
            if nums[i]%3==0 and nums[i]%2==0:
                sum+=nums[i]
                count+=1
        if count>0:
            return sum/count
        else:
            return count
        
