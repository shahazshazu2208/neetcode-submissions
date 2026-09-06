class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        mprofit=0
        for price in prices:
            minprice= min(price,minprice)
            if minprice < price:
                cprofit=price-minprice
                mprofit=max(mprofit,cprofit)
        return mprofit
sol = Solution()
print(sol.maxProfit([10,1,5,6,7,1]))

        