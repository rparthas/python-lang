from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
     idx = 0
     max_profit = 0
     for i in range(1, len(prices)):
         if prices[i] > prices[idx]:
             max_profit = max(max_profit, prices[i] - prices[idx])
         else:
             idx = i
     return max_profit


if __name__ == '__main__':
    prices = [10,2,5,6,7,1,8]
    print(Solution().maxProfit(prices))
