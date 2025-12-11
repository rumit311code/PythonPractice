"""
Using sliding window

This algorithm maintains a sliding window (substring) defined by indices left and right.
It expands right while characters are unique, and when a repeating character occurs,
it shrinks from the left to remove duplicates.
The time complexity is O(n) since each character is visited at most twice.
"""

## To return only the length of the string.
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        print(f"char_set 1|{char_set}|===l|{left}|===|{s[left]}|====r|{right}|===|{s[right]}|")
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        print(f"char_set 2|{char_set}|")
        char_set.add(s[right])
        print(f"char_set 3|{char_set}|")
        print(f"==============")
        max_length = max(max_length, right - left + 1)

    return max_length


# Example usage
# input_str = "abcabcbb"
# print(length_of_longest_substring(input_str))  # Output: 3

## To return the string itself.
def longest_substring_without_duplicates(s: str) -> str:
    char_index_map = {}
    left = 0
    max_length = 0
    start_index = 0

    for right in range(len(s)): # O(n)
        print(f"====left: {left}, right: {right},char_index_map: {char_index_map}")
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        char_index_map[s[right]] = right
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start_index = left
        print(f"====left: {left}, right: {right}, max_length|{max_length}|, char_index_map: {char_index_map}")
    print(f"max_length |{max_length}|, start index|{start_index}|, right |{right}|")
    return s[start_index:start_index + max_length] # O(n)

# Example usage:
input_str = "abcabcdbb"
result = longest_substring_without_duplicates(input_str)
print(f"Largest substring without duplicate characters: '{result}'") # Output: "abc"

