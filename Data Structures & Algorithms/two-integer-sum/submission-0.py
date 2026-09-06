class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        seen={}
        for i in range(l):
            diff=target-nums[i]
            if diff in seen:
                return [seen[diff][0], i]
            if nums[i] not in seen:
                seen[nums[i]]=[]
            seen[nums[i]].append(i)