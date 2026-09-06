class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        while left < right:
            csum = numbers[left]+numbers[right]

            if csum == target:
                return [left+1,right+1]
            
            elif csum < target:
                left +=1
            
            else:
                right -= 1
sol = Solution()
print(sol.twoSum([1, 2, 3, 4], 3))    
print(sol.twoSum([2, 7, 11, 15], 9))    
        