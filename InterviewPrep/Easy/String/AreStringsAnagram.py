"""
https://neetcode.io/problems/is-anagram/question

Video: https://www.youtube.com/watch?v=9UtInBqnCgA

Valid Anagram

Given two strings s and t, return true if the two strings are anagrams of each other,
otherwise return false.

An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
s and t consist of lowercase English letters.
"""

def are_anagrams1(s1, s2):
    # Normalize by removing spaces and converting to lowercase
    s1 = s1.replace(" ", "").lower() # O(n)
    s2 = s2.replace(" ", "").lower()

    # Check if sorted characters are equal
    return sorted(s1) == sorted(s2) #O(nlogn)
    """
    Runtime: O(nlogn)
    Space: O(1) if no replace or sort in pace. otherwise O(n)
    """

def are_anagrams2(s1, s2): # hashmap O(n)
    return Counter(s1) == Counter(s2)
    """
    Runtime: O(n)
    Space: O(n) for 2 counters.
    """

# Example usage
string1 = "listen"
string2 = "Silent"
print(are_anagrams1(string1, string2))  # Output: True

string3 = "hello"
string4 = "world"
print(are_anagrams1(string3, string4))  # Output: False