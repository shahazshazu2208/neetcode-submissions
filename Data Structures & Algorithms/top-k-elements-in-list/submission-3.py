class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sortednums = sorted(count.items() , key=lambda x:x[1] , reverse=True)
        sortednums = sortednums[:k]
        return [num for num, freq in sortednums]
        