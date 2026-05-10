class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1
        max_profit = 0
        n = len(prices)

        while right < n:
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            
            right += 1

        return max_profit