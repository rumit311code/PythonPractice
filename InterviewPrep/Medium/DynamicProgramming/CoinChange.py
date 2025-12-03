"""
https://neetcode.io/problems/coin-change

Coin Change

You are given an integer array coins representing coins of different denominations
(e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount.
If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.

Example 1:
Input: coins = [1,5,10], amount = 12
Output: 3
Explanation: 12 = 10 + 1 + 1. Note that we do not have to use every kind coin available.

Example 2:
Input: coins = [2], amount = 3
Output: -1
Explanation: The amount of 3 cannot be made up with coins of 2.

Example 3:
Input: coins = [1], amount = 0
Output: 0
Explanation: Choosing 0 coins is a valid way to make up 0.

Constraints:
1 <= coins.length <= 10
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10000
"""
from typing import List

# Follow same approach as Climbing Stairs (bottoms up) with a decision tree.
# top-down: recursive dfs, for an amount, branch for each coin, cache to store prev coin_count
# for each amount; bottom-up: compute coins for amount = 1, up until n,
# using for each coin (amount - coin), cache prev values
#
# target:7, coins=[1,3,4,5]
# dp[n] = 1 + dp[n - coin value] -> count from 0 to the target.
#
# dp[0] = 0
#   because all coins are more than 0, so no need to count. so set dp[0] = 0
# dp[1] = 1 + dp [1(n) - 1(coin value)] = 1 + dp[0] = 1 + 0 = 1
#   coin 3, 4 and 5 are more than 1, so no need to count. So the min for dp[1] = 1
# dp[2] = 1 + dp[2 - 1] = 1 + dp[1] = 1 + 1 = 2
#   coin 3, 4 and 5 are more than 2, so no need to count. So the min for dp[2] = 2
# dp[3] = 1 + dp[3 - 1] = 1 + dp[2] = 1 + 2 = 3
# dp[3] = 1 + dp[3 - 3] = 1 + dp[0] = 1 + 1 = 1
#   coin 4 and 5 are more than 3, so no need to count. So the min for dp[3] = 1
# dp[4] = 1 + dp[4 - 1] = 1 + dp[3] = 1 + 1 = 2
# dp[4] = 1 + dp[4 - 3] = 1 + dp[1] = 1 + 1 = 2
# dp[4] = 1 + dp[4 - 4] = 1 + dp[0] = 1 + 0 = 1
#   coin 5 is more than 4, so no need to count. So the min for dp[4] = 1
# dp[5] = 1 + dp[5 - 1] = 1 + dp[4] = 1 + 1 = 2
# dp[5] = 1 + dp[5 - 3] = 1 + dp[2] = 1 + 2 = 3
# dp[5] = 1 + dp[5 - 4] = 1 + dp[1] = 1 + 1 = 2
# dp[5] = 1 + dp[5 - 5] = 1 + dp[0] = 1 + 0 = 1
#   So the min for dp[5] = 1
# dp[6] = 1 + dp[6 - 1] = 1 + dp[5] = 1 + 1 = 2
# dp[6] = 1 + dp[6 - 3] = 1 + dp[3] = 1 + 1 = 2
# dp[6] = 1 + dp[6 - 4] = 1 + dp[2] = 1 + 2 = 3
# dp[6] = 1 + dp[6 - 5] = 1 + dp[1] = 1 + 1 = 2
#   So the min for dp[6] = 2
# dp[7] = 1 + dp[7 - 1] = 1 + dp[6] = 1 + 2 = 3
# dp[7] = 1 + dp[7 - 3] = 1 + dp[4] = 1 + 1 = 2
# dp[7] = 1 + dp[7 - 4] = 1 + dp[3] = 1 + 1 = 2
# dp[7] = 1 + dp[7 - 5] = 1 + dp[2] = 1 + 2 = 3
#   So the min for dp[7] = 2 -> Answer

class Solution:
    def coinChange(self, coins: List[int], target: int) -> int:
        dp = [target + 1] * (target + 1) # dp[8,8,8,8,8,8,8,8]
        print(f"dp: {dp}")
        dp[0] = 0 # base case for any target because no coins needed for amount 0.

        for amount in range(1, target + 1): # O(amount) loop -> [1,2,3,4,5,6,7]
            print(f"amount: {amount} | dp: {dp}")

            for coin in coins: # O(len(coins)) loop
                # this might cause problems for large inputs. so, comment out if running for large array.
                print(f"coin: {coin} | a-c: {amount-coin} | dp: {dp}")

                # if adding a coin will result in amount more than the target, ignore it.
                if amount - coin >=0:
                    dp[amount] = min(dp[amount], 1 + dp[amount - coin])
                print("-----")
            print("=====")

        # target + 1 is the default value we set in line75.
        # for a target of 7, dp[7] should not be 8.
        # if it is 8 then no coin combinations were found that add up to 7.
        return dp[target] if dp[target] != (target + 1) else -1

print(f"coins=[1,3,4,5], target=7 |{Solution().coinChange([1,3,4,5],7)}|")
""" 
Runtime: O(amount * len(coins))
Space: O(amount) to store the dp
"""