class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max =  0
        small = 1000
        sliding = False
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                if not sliding:
                    if prices[i]<small:
                        small = prices[i]
                    sliding = True
                if max < prices[i+1] - small:
                    max = prices[i+1] - small
            else:
                sliding = False
        return max