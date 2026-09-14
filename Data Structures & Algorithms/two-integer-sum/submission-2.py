class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff][0],i]
            if nums[i] not in seen:
                seen[nums[i]]=[]
            seen[nums[i]].append(i)

        