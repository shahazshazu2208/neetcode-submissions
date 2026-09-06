class Solution:
    def hasDuplicate(self, nums):
        dict={}
        for i in nums:
            if i in dict:
                dict[i]=dict[i]+1
            else:
                dict[i]=1
        for i in dict:
            if dict[i]>1:
                return True
        return False