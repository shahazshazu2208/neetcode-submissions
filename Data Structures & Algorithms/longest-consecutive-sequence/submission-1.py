class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=0

        for num in nums:
            if(num-1) not in num_set:
                cnum = num
                cstreak=1

                while(cnum+1) in num_set:
                    cnum = cnum + 1
                    cstreak +=1
                
                longest= max(longest,cstreak)
        return longest
                


sol = Solution()
print(sol.longestConsecutive([2, 20, 4, 10, 3, 4, 5]))  
print(sol.longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]))           


            

        