"""
https://neetcode.io/problems/buy-and-sell-crypto

Best Time to Buy and Sell Stock

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:
Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:
Input: prices = [10,8,7,5,2]
Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

    1 <= prices.length <= 100
    0 <= prices[i] <= 100

"""
from typing import List

# left pointer for day1 (i)
# right pointer for day2 (i+1)
# R < L, loss or no gain, update the left pointer to right
# R >= L, calculate current profit, if more than previous, update profit, move R
# iterate

class Solution:
    def max_profit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]: # profit, no need to change left pointer.
                max_profit = max(max_profit, prices[r] - prices[l])
            else: # loss or no gain, move left pointer.
                l = r # move left pointer to right.
            r += 1 # keep moving right pointer in each iteration.

        return max_profit

print(f"max profit |{Solution().max_profit([10,1,5,6,1,7,1])}|")
print(f"max profit |{Solution().max_profit([1,1,1,1])}|")
"""
Run time: O(n) because scanning prices array only once.
Space: O(1) to store profit.
"""