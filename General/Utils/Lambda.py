###### Basic Lambda Syntax
# A lambda function with a single argument, adding 10 to the input:
x = lambda a: a + 10
print(x(5))  # Output: 15

###### Lambda with Multiple Arguments
# Multiplying two arguments:
x = lambda a, b: a * b
print(x(5, 6))  # Output: 30

# Summing three arguments:
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))  # Output: 13

###### Lambda Inside Functions
# Lambda returning a closure (multiplier function):
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
print(mydoubler(11))  # Output: 22

###### Using Lambda with map() and filter()
# Doubles each element in a list:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]

# Filters even numbers from a list:
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: x % 2 == 0, my_list))
print(new_list)  # Output: [4, 6, 8, 12]

###### Lambda for Sorting
# Sort a list of tuples by the second value:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # Output: [('Tobias', 22), ('Emil', 25), ('Linus', 28)]

# Sort list of strings by length:
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['pie', 'apple', 'banana', 'cherry']