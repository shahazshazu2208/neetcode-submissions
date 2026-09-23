class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        n=len(arr)
        csum=sum(arr[:k])
        msum=csum
        for i in range(1,k+1):
            csum += arr[n-i] - arr[k-i]
            msum=max(msum,csum)
        return msum
        
        