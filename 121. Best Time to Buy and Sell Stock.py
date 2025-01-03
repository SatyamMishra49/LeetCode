class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _max = 0
        l, r = 0, 1
        while l < r and r < len(prices):
            currMax = 0
            if prices[l] <= prices[r]:
                currMax = prices[r] - prices[l]
                _max = max(_max, currMax)
                r += 1
            else:
                l = r
                r += 1
        return _max
