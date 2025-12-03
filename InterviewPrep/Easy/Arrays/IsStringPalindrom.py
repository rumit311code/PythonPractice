def is_palindrome(string):
    # Normalize the string to lowercase to make the check case-insensitive
    string = string.lower() # use this if only for case-insensitive.
    # Check if the string is equal to its reverse
    if string == string[::-1]:
        # string[start:end:step]
        #   start is the index where slicing begins (inclusive, default is 0).
        #   end is the index where slicing stops (exclusive, default is the end of the string).
        #   step is the interval between characters taken (default is 1).
        #   step = -1 means slice is taken backwards, from the end of the string to the start.
        return True
    else:
        return False

# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

"""
Runtime: O(n): to compares the string to its reverse, and reversing the string involves traversing all n characters once.
Space: O(n): slicing operation string[::-1] creates a reversed copy of the string
"""