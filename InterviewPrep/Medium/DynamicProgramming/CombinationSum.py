"""
https://neetcode.io/problems/combination-target-sum

video: https://www.youtube.com/watch?v=GBKI9VSKdGg -> 9:52

Combination Sum

You are given an array of distinct integers nums and a target integer target.
Your task is to return a list of all unique combinations of nums where
the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times.
Two combinations are the same if the frequency of each of the chosen numbers is the same,
otherwise they are different. So, [3,2,2] and [2,3,2] are same.

You may return the combinations in any order and
the order of the numbers in each combination can be in any order.

Example 1:
Input:
nums = [2,5,6,9]
target = 9
Output: [[2,2,5],[9]]
Explanation:
2 + 2 + 5 = 9. We use 2 twice, and 5 once.
9 = 9. We use 9 once.

Example 2:
Input:
nums = [3,4,5]
target = 16
Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

Example 3:
Input:
nums = [3]
target = 5
Output: []

Constraints:

All elements of nums are distinct.
1 <= nums.length <= 20
2 <= nums[i] <= 30
2 <= target <= 30
"""
from typing import List

# use depth first search with binary decision.
# one branch includes the number, another one does not.
# continue until all branches are covered.
# worst case depth will be of the length equal to the target.
# since this is a binary tree, run time is 2^(target).
#
# sort the input num array if not done. so nums = [2,3,6,7]
#
# Binary decision tree. The tree ends when total is > 7 for example [2,2,2,2]=8.
# when the total=target e.g. [2,2,3] = 7, save the pair, stop looking further and goto the right branch.
# the left side picks a num and that num is not used to make pairs on the right side.
# so from [2], two branches. one that adds 2 e.g. [2,2]. another one that does NOT e.g. just [2]
# the left branch [2,2] continues in similar way and branches off at each step.
# the right branch keeps adding one new number at each step.
#
#                                   [start=0]
#                        [2(i=0)]                       []
#                [2,2]          [2]          [3(i=1)]           []
#          [2,2,2]   [2,2]   [2,3][2]         ..|..  [6(i=2)]        []
#  [2,2,2,2]=8  [2,2,3] [2,2]  ..|..              [6,7]=13    [7(i=3)][]
#                  [2,2,6] [2,2,7]


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # i -> num in nums.
            # cur -> List[List[int]] number pairs already visited e.g. [[2,2], [2,2,3]]
            # total -> that should match the target.
            print(f"==================================")
            print(f"i: {i}, cur: {cur}, total: {total}, res: {res}")
            if total == target: # pair of numbers found that match the target.
                res.append(cur.copy()) # use copy of cur because cur is continuously updated.
                return
            if i >= len(nums) or total > target:
                # i >= len(nums) -> array out of bound
                # total > target -> total more than target e.g. [2,6]=8 > 7.
                return

            print(f"i: {i}, nums[i]: {nums[i]}")
            cur.append(nums[i])
            print(f"cur1: {cur}")

            # first recursive call that includes the num.
            # for i=0, num[i]=2, cur[2], total = 0 + 2 = 2.
            print(f"calling FIRST DFS.")
            dfs(i, cur, total + nums[i])
            print(f"FIRST DFS completed.")
            print(f"cur2: {cur}")

            cur.pop()
            # pops 2 from cur. so now, cur[...] without 2.
            print(f"cur3: {cur}")

            # second recursive call that does NOT include the num.
            # for i+1=0+1=1, num[1]=3, cur[[... ], 3], total = 0 = 0.
            print(f"calling SECOND DFS.")
            dfs(i + 1, cur, total)
            print(f"SECOND DFS completed.")
            print(f"cur4: {cur}")

        dfs(0,[],0)
        return res

# print(f"[2,3,6,7] - 7 ===> |{Solution().combinationSum(nums=[2,3,6,7], target=7)}|")
"""
Runtime: O(2^target)
Space: O(1)
"""

# brute-force approach.
class Solution1:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        count=0
        for i in range(len(nums)): # first loop: O(n)
            count += 1
            print(f"===== i: {i}, nums[i]: {nums[i]} =====")
            if nums[i] == target:
                if [nums[i]] not in res:
                    res.append([nums[i]])
                continue
            elif nums[i] > target:
                continue
            total = nums[i]
            cur = [nums[i]] # [2]
            for j in range(i, len(nums)): # second loop: O(n). so O(n*n)
                count += 1
                print(f"----- i: {i}, j: {j}, nums[j]: {nums[j]} -----")
                print(f"START1: total: {total}, cur: {cur}")
                total += nums[j]
                print(f"START1A: total: {total}")
                while total > target and cur:
                    count += 1
                    total -= nums[j-1]
                    cur.pop()
                    print(f"START1B: total: {total}, cur: {cur}")
                print(f"START2: total: {total}, cur: {cur}")
                cur.append(nums[j]) # [2,2]
                if total == nums[i+1] and cur[0] == nums[i+1]:
                    break
                print(f"START3: total: {total}, cur: {cur}")
                while total < target: # third loop: O(target)
                    count += 1
                    total += nums[j]
                    cur.append(nums[j])  # [2,2,2]
                    print(f"START4: total: {total}, cur: {cur}")
                if total == target:
                    if cur not in res:
                        res.append(cur.copy())
                    print(f"END1: res: {res}")
                    break
                elif total > target: # cur=[2,2,2,2]
                    total -= nums[j] # total= 8-2 = 6
                    cur.pop() # cur=[2,2,2] remove the last num from cur and go to the next num.
                    print(f"END2: total: {total}, cur: {cur}")
        print(f"count: {count}")
        return res
# |[[2, 2, 3], [7]]|
print(f"[2,3,6,7] - 7 ===> |{Solution1().combinationSum(nums=[2,3,6,7], target=7)}|")

"""
Runtime: O(n*n*target) worst case. however, the avg case should be less than that because the code above avoids dups.
Space: O(n) to store List[List[int]] pairs
"""