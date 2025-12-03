import re

"""
This example FINDS every character between 'a' and 'e' in the string and returns them as a list.
"""
pattern1 = r"[a-e]"
text1 = "Aye, said Mr. Gibenson Stark"
matches = re.findall(pattern1, text1)
print(matches)
# Output: ['e', 'a', 'd', 'b', 'e', 'a']

"""
This SPLITS the string at each sequence of digits.
"""
pattern2 = r'\d+'
text2 = 'Twelve:12 Eighty nine:89.'
result2 = re.split(pattern2, text2)
print(result2)
# Output: ['Twelve:', ' Eighty nine:', '.']

"""
This REPLACES every whitespace character with the number '9'.
"""
text3 = "The rain in Spain"
x = re.sub(r"\s", "9", text3)
print(x)
# Output: 'The9rain9in9Spain'

"""
This SEARCHES for three consecutive digits in a string and returns the FIRST match ANYWHERE in the string. 
If the pattern is NOT found anywhere, it returns None.
"""
match = re.search(r"[0-9][0-9][0-9]", "foo456bar678")
print(match.group())
# Output: '456'

"""
Explanation:
    re.match() tries to MATCH the pattern at the start of the string.
    group(0) returns the entire matched substring.
    group(1), group(2), etc. return the captured groups defined by parentheses in the regex.
    If there's no match, match will be None.

For the text "Hello World" and pattern r"(\w+) (\w+)", this code outputs:

Full match: Hello World
First group: Hello
Second group: World

This example shows how to extract parts of a matched string with capturing groups using regex in Python.
"""
pattern = r"(\w+) (\w+)"
text = "Hello World"

match = re.match(pattern, text)
if match:
    print("Full match:", match.group(0))  # prints Hello World
    print("First group:", match.group(1)) # prints Hello
    print("Second group:", match.group(2))# prints World
    print("third: ", match.groups()) # prints ('Hello', 'World')
else:
    print("No match found")

"""
Search vs Match
"""
print(re.match(r"hello", "hello world"))  # Matches at start, returns a match object
print(re.match(r"world", "hello world"))  # No match at start, returns None
print(re.search(r"world", "hello world")) # Finds 'world' anywhere, returns a match object
match = re.search(r"world", "hello world")
print(f"asdfasdf ====" + match.group())

"""
re iterator

To find all occurrences of a regex pattern and their indices in a string in Python, 
you can use the re.finditer() function from the re module. This function returns an iterator yielding match objects 
for all non-overlapping matches of the pattern in the string. Each match object has methods start(), end(), and span() 
that give the start index, end index, and both indices as a tuple, respectively.
"""
pattern = re.compile(r'your_pattern_here')  # Compile regex pattern
text = "your sample text here to search"

for match in pattern.finditer(text):
    print(f"Match at {match.start()} to {match.end() - 1}: {match.group()}")

# match.start() gives the starting index of the match.
# match.end() gives the index just after the last character of the match (so end - 1 is the last character index).
# match.group() returns the matched substring.
