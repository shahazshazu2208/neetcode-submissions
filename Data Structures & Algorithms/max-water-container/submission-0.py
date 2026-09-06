class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0 , len(heights)-1
        marea=0
        while left < right :
            cheights = min(heights[left],heights[right])
            cwidth = right - left
            carea = cheights * cwidth
            marea = max(marea,carea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return marea
sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49 (between height 8 at index 1 and 7 at index 8)
print(sol.maxArea([1, 1]))

        