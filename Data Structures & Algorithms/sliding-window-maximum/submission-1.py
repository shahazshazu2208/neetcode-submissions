from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxlist=[]
        dq = deque()
        for i in range(len(nums)):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

            if dq[0] <= i-k:
                dq.popleft()
            
            if i >= k-1 :
                maxlist.append(nums[dq[0]])
        return maxlist
    
        