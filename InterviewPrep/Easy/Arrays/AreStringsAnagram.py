def are_anagrams(s1, s2):
    # Normalize by removing spaces and converting to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Check if sorted characters are equal
    return sorted(s1) == sorted(s2)


# Example usage
string1 = "listen"
string2 = "Silent"
print(are_anagrams(string1, string2))  # Output: True

string3 = "hello"
string4 = "world"
print(are_anagrams(string3, string4))  # Output: False