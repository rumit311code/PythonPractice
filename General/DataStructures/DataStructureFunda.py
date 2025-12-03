"""
Find a dictionary key with the highest value.
"""
my_dict = {'apple': 10, 'banana': 30, 'cherry': 20, 'date': 40}
# Using max() with the dictionary's .get method as the key for comparison
key_with_max_value = max(my_dict, key=my_dict.get)
print(f"The key with the maximum value is: {key_with_max_value}")

"""
Mutable: list, dict, set, bytearray
- Definition: Objects whose internal state can be changed after they are created.
- How they work: Operations that modify the object change it in place, without creating a new object.
- Use cases: Useful when you need to update the contents of a data structure frequently, like an employee list.
- Note: Mutable objects cannot be used as keys in a dictionary or elements in a set, because their contents 
    (and therefore their hash value) could change.

Immutable: int, float, str, tuple, bool, frozenset
- Definition: Objects whose state cannot be modified after they are created.
- How they work: Any operation that appears to modify an immutable object actually creates and returns a new object.
- Use cases: Ideal for situations where you need data to remain constant, ensuring its integrity and consistency.
- Note: Immutable objects are safe to use as dictionary keys and set elements because their hash value will never change.

1. When the Compound Object Contains Only Immutable Elements:
If a list, tuple, or other compound object contains only immutable elements 
(such as integers, floats, strings, or other tuples), a shallow copy behaves effectively like a deep copy for those elements. 
This is because immutable objects cannot be changed in place; any "modification" actually creates a new object. 
Therefore, sharing references to immutable objects does not lead to unintended side effects.
"""

original_list = [1, 2, "hello"]
shallow_copy_list = list(original_list) # Or original_list.copy()
# This creates a new integer object 5 and assigns it to shallow_copy_list[0] and
# does NOT modify original_list[0] which is still pointing at 1 (and not 5).

shallow_copy_list[0] = 5 # updates only shallow_copy_list.
shallow_copy_list[2] = "world" # updates only shallow_copy_list.

print(original_list) # Output: [1, 2, 'hello']
print(shallow_copy_list) # Output: [5, 2, 'world']

original_list[0] = 10 # updates only original_list.
original_list[2] = "hello2" # updates only original_list.

print(original_list) # Output: [10, 2, 'hello2']
print(shallow_copy_list) # Output: [5, 2, 'world']

"""
2. When You Need a Separate Container but are Okay with Shared Nested References: 
If you need a new top-level container object (e.g., a new list or dictionary) 
but are fine with its elements still referencing the same objects as the original, a shallow copy is suitable. 
This is common when you might modify the structure of the container (add/remove elements) 
but don't intend to modify the nested mutable objects themselves, or if modifying them is acceptable 
because the original also reflects those changes.
"""
original_list_of_lists = [[1, 2], [3, 4]]
shallow_copy_list_of_lists = original_list_of_lists.copy()

shallow_copy_list_of_lists.append([5, 6]) # Modifies only shallow_copy_list_of_lists and NOT original_list_of_lists
# When you append() an item to a shallow-copied list, you are adding a NEW reference to a NEW object (the appended item)
# to the end of the COPIED list. This operation modifies the structure of the COPIED list itself by extending it,
# but it does NOT change any of the EXISTING objects that both the ORIGINAL and COPIED lists were referencing.
# Since the original list is a separate list object, its structure remains unchanged.

print(original_list_of_lists) # Output: [[1, 2], [3, 4]] # no change to original list.
print(shallow_copy_list_of_lists) # Output: [[1, 2], [3, 4], [5, 6]]

shallow_copy_list_of_lists[0][0] = 99 # change by REFERENCE of an EXISTING element
# Modifies a nested mutable object (shared reference).
# This modifies the *actual nested list object* at index 0.
# so both original_list_of_lists and shallow_copy_list_of_lists are modified.

# When you update an item in a shallow-copied list using its index (e.g., shallow_copy[0] = new_value),
# you are changing the reference stored at that index within the copied list to point to a different object (new_value).
# If the item at that index was a mutable object (like another list or a dictionary) and
# both the original and shallow-copied lists were referencing the same mutable object,
# then changing the content of that mutable object through one list will be reflected in the other.

print(original_list_of_lists) # Output: [[99, 2], [3, 4]] (Original is affected)
print(shallow_copy_list_of_lists) # Output: [[99, 2], [3, 4], [5, 6]]

"""
DEEP COPY
"""
import copy

original = [[1, 2, 3], [4, 5, 6]]  # example nested list
deep_copied = copy.deepcopy(original)

# Modifications to the original will not affect the deep copy
original[0][0] = 99 # does NOT change "deep_copied"
print(original)       # Output: [[99, 2, 3], [4, 5, 6]]
print(deep_copied)    # Output: [[1, 2, 3], [4, 5, 6]]

"""
3. For Performance Optimization with Large, Complex Structures:
Creating a deep copy of a very large and deeply nested data structure can be computationally expensive and 
consume significant memory. If the specific use case allows for shared references to nested mutable objects 
without causing issues, a shallow copy offers a more efficient alternative.

In summary, choose a shallow copy when:
- Your compound object contains only immutable elements.
- You need a new top-level container but are comfortable with nested mutable objects being shared by reference, 
    or you do not intend to modify them.
- Performance is a critical concern, and the implications of shared references are understood and acceptable.
"""