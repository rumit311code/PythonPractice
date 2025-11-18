from collections import Counter

def first_non_repeating_char(s):
    # Count frequency of each character
    char_count = Counter(s)
    print(f"char_count |{char_count}")
    # Iterate over string to find first char with count 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None  # If no non-repeating character found


# Example usage
input_str = "swiss"
result = first_non_repeating_char(input_str)
if result:
    print(f"First non-repeating character: {result}")
else:
    print("No non-repeating character found.")