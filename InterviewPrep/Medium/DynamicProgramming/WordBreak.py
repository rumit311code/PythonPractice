"""
https://neetcode.io/problems/word-break

Word Break

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times.
You may assume all dictionary words are unique.

Example 1:
Input: s = "neetcode", wordDict = ["neet","code"]
Output: true
Explanation: Return true because "neetcode" can be split into "neet" and "code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen","ape"]
Output: true
Explanation: Return true because "applepenapple" can be split into "apple", "pen" and "apple".
Notice that we can reuse words and also not use all the words.

Example 3:
Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]
Output: false because "cars" is not there in the dictionary.

Constraints:
1 <= s.length <= 200
1 <= wordDict.length <= 100
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
"""
from typing import List


class Solution1:
    # for each prefix, if prefix is in dict and wordbreak(remaining str)=True,
    # then return True, cache result of wordbreak;

    # use dynamic programming from bottom up
    # start from last index and keep matching each word in the word dict
    # start with dp[len(s)] = True and then keep iterating until dp[0] for the len(s)
    # For s=neetcode | wordDict=['neet','code']
    # for each word length of wordDict do the following
    #
    # formula: dp[i] = dp[i + len(word)]
    #
    # dp[8] = empty string = True
    # dp[7] = e = False
    # dp[6] = de = False
    # dp[5] = ode = False
    # dp[4] = code = True # found in wordDict
    # dp[3] = tcode = False
    # dp[2] = etcode = False
    # dp[1] = eetcode = False
    # dp[0] = neetcode = True (0 + dp[len(word)]) found in wordDict
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1): # O(n) loop
            for w in wordDict: # O(m) loop
                if (i+len(w)) <= len(s) and s[i: i + len(w)] == w: # O(n) check
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
print(f"s=neetcode | wordDict=['neet','code'] |{Solution1().wordBreak(s="neetcode", wordDict=['neet','code'])}|")
print(f"s=catsincars | wordDict=['cats','cat','sin','in','car'] |{Solution1().wordBreak(s="catsincars", wordDict=['cats','cat','sin','in','car'])}|")
print(f"s=aaaaaaa | wordDict=['aaaa','aaa'] |{Solution1().wordBreak(s="aaaaaaa", wordDict=['aaaa','aaa'])}|")

"""
Runtime: O(n.m.n) -> m = wordDict length, n = len(s)
Space: O(n)
"""

class Solution2: # DOES NOT WORK for s=aaaaaaa | wordDict=['aaaa','aaa']
    # Solution1: Brute force: DO NOT USE
    #   check character by character and see if there is a matching word in the dict.
    #       if a word is found, start a new word again from that index.
    #       for s = "neetcode" and wordDict = ["leet", "code"]
    #           start with character "n" and see if its present in the wordDict
    #           repeat until a full match is found.
    #           in this case first match will be at "neet"
    #           after that start again with "c" and continue the same.
    #           at the end if a full match is found -> answer true otherwise false
    # Does not work for s=aaaaaaa | wordDict=['aaaa','aaa']

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_segments = []
        match_found = False
        start_index = 0
        for i in range(1, len(s)+1): # O(n) loop
            match_found = False
            print(f"start_index = {start_index} | i = {i}")
            print(f"s[start_index:i] = |{s[start_index:i]}|")
            if s[start_index:i] in wordDict: # match found
                word_segments.append(s[start_index:i])
                start_index = i
                match_found = True
        print(f"word_segments: {word_segments} | match_found: {match_found}")
        return match_found