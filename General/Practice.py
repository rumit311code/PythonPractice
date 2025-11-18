from typing import List

def get_count(timestamps: List[int], start: int, end: int) -> int:
    start_index = 0
    end_index = 0
    for i in range(len(timestamps)): # O(n)
        if timestamps[i] <= start:
            start_index += 1

        if timestamps[i] <= end:
            end_index += 1
    print(f"start_index: {start_index}, end: {end_index}")
    return len(timestamps[start_index:end_index + 1])  # O(n)

print(get_count(timestamps=[1, 3, 5, 7, 9, 11], start=3, end=7))
exit(0)
    # mid = (start_index + end_index) // 2

    # if timestamps[mid] >= start
    #     start_index -= mid

    # if timestamps[mid] <= start
    #     end_index += mid

    # while start_index > 0 or end_index < len(timestamps):
    #     # if timestamps[start_index] <= start:
    #     #     start_index += 1
    #
    #     # if timestamps[end_index] <= end:
    #     # end_index -= 1
    #     if timestamps[mid] >= start
    #         start_index -= mid
    #
    #     if timestamps[mid] <= end
    #         end_index += mid


print(17/5) # floating number
print(17//5) # remainder
print(17%5) # quotient

lst1 = [1,2,3]
lst2 = [4,5]
print(lst1)
lst1.extend(lst2)
print(lst1)

original_list_of_lists = [0, [1, 2], [3, 4]]
shallow_copy_list_of_lists = original_list_of_lists.copy()

shallow_copy_list_of_lists.append([5, 6])

print(original_list_of_lists)
print(shallow_copy_list_of_lists)

shallow_copy_list_of_lists[1][0] = 99
print(original_list_of_lists)
print(shallow_copy_list_of_lists)

original_list_of_lists[1][0] = 100
print(original_list_of_lists)
print(shallow_copy_list_of_lists)


shallow_copy_list_of_lists[0] = 11
print(original_list_of_lists)
print(shallow_copy_list_of_lists)

original_list_of_lists[0] = 13
print(original_list_of_lists)
print(shallow_copy_list_of_lists)


print(17/5)
print(17//5)
print(17%5)

print(bin(2))
print(bin(-2))

s = "Hello"

print(f"list |{list(s)}|")
print(f"set |{set(s)}|")

lst = []
import sys
print(sys.getsizeof(lst))  # Initial size in bytes

for i in range(10):
    lst.append(i)
    print(f'Length: {len(lst)}, Size: {sys.getsizeof(lst)}')


dp = [0] * (2)
print(dp)

a = 3
b = 2

print(bin(a))
print(bin(b))
print(a ^ b)
print(a & b)
print(a & b << 1)

