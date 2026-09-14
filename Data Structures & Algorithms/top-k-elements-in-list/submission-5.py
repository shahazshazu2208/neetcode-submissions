class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sortednums = sorted(count.items() , key=lambda x:x[1] , reverse=True)
        return [num[0] for num in sortednums[:k]]
        