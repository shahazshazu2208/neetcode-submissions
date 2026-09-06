class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left , right = 0,len(height)-1
        lmax , rmax = height[left],height[right]
        trapped=0

        while left<right:
            if lmax < rmax:
                left +=1
                lmax=max(lmax,height[left])
                trapped += lmax - height[left]
            
            else:
                right -= 1
                rmax = max(rmax,height[right])
                trapped += rmax - height[right]

        return trapped
sol = Solution()
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Output: 6
print(sol.trap([4, 2, 0, 3, 2, 5]))