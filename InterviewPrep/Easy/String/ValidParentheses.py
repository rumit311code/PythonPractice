"""
https://neetcode.io/problems/validate-parentheses/question

Video: https://www.youtube.com/watch?v=WTzjTskDFMg

Valid Parentheses

You are given a string s consisting of the following characters:
'(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "[]"
Output: true

Example 2:
Input: s = "([{}])"
Output: true

Example 3:
Input: s = "[(])"
Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:
1 <= s.length <= 1000
"""

class Solution:
    def isValid(self, s: str) -> bool:
        close_open_dict = {
            ")": "(",
            "}": "{",
            "]":"["
        }
        stack = []
        # "([{}])"
        for char in s:
            print(f"char: {char}, stack: {stack}")
            if char in close_open_dict:
                # the current char is a closing parenthesis.
                # so the previous char must match its opening parenthesis.
                # the previous char is the LAST element inserted in the stack.
                # stack[-1] -> gives the last element of the stack.
                # which should match its opening parentheses from the dict.

                print(f"-----checking opening char for a closing char |{char}|")
                if stack and stack[-1] == close_open_dict[char]:
                    # remove the last char (opening parenthesis that matched) from the stack.
                    stack.pop() # pop() removes the last item from stack.
                    print(f"----- -----updated stack: {stack}")
                else:
                    # open and close parenthese don't match or stack is empty.
                    print(f"----- -----opening parenthesis not found for char |{char}|, returning false.")
                    return False
            else:
                # current char is an opening parentheses. add it to the stack.
                print(f"-----adding opening char |{char}| to stack.")
                stack.append(char)
                print(f"-----updated stack: {stack}")

        return True if not stack else False

print(Solution().isValid("([{}])"))


