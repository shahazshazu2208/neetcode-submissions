class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        out = [1]*n
        p=1
        for i in range(n):
            out[i]=p
            p=p*nums[i]
        
        s=1
        for i in range(n-1,-1,-1):
            out[i]=out[i]*s
            s=s*nums[i]
        return out

        


sol = Solution()
print(sol.productExceptSelf([1,2,4,6]))    