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
                left+=1
            else:
                right-=1
        return marea


        