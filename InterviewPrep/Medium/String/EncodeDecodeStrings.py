"""
https://neetcode.io/problems/string-encode-and-decode/question

Video: https://www.youtube.com/watch?v=B1k_sxOSgv8

Encode and Decode Strings

Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        # add the length and some delimiter before each word.
        # ["neet","code","love","you"]
        # 4#neet4#code4#love3#you're
        # Using the combination of a number and some character(# in this case) to encode
        # helps with avoiding edge cases with strings that have some number OR delimiter char.
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(f"encoded str : {res}")
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find the '#' that ends the length.
            # This will ensure the lengths of more than 1 digit is also accounted for e.g. 10.
            j = i
            while s[j] != '#':
                j += 1

            # s[i:j] is the length substring (can be multiple digits).
            length = int(s[i:j])

            # the string starts after '#'. j = index of #.
            start = j + 1 # optional variable. can be skipped.
            end = start + length # optional variable. can be skipped.
            res.append(s[start:end])
            print(f"----decoded strs : {res}")
            # move to next encoded string.
            i = end
        print(f"FINAL decoded strs : {res}")
        return res


encoded_str = Solution().encode(["we","say",":","yes","!@#$%3#*()"])
decoded_str = Solution().decode(encoded_str)
