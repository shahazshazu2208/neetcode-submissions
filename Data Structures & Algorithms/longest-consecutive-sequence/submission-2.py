class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=0
        for num in nums:
            if (num-1) not in num_set:
                cnum=num
                cstreak=1

                while (cnum+1) in num_set:
                    cnum+=1
                    cstreak+=1
                longest=max(longest,cstreak)
        return longest
        
                


            

        