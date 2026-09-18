class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        mprofit=0
        for price in prices:
            minprice = min(price,minprice)
            profit = price-minprice
            mprofit = max(profit,mprofit)
        return mprofit

        