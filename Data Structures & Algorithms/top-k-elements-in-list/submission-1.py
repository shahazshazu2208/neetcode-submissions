class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        sortedpair=sorted(count.items(),key=lambda item:item[1],reverse=True)
        top_k=[]
        for i in range(k):
            num,freq=sortedpair[i]
            top_k.append(num)
        return top_k

sol = Solution()
print(sol.topKFrequent([1, 2, 2, 3, 3, 3], 2))
        