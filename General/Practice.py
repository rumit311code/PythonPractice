# dp = {}
# dp1 = ()
dp = {}

dp["info"] = dp.get("info", 0) + 1
print(dp["info"])
print(dp)
from typing import List

container: List[int] = []
print(container)

lst1 = [1,2,3,4,5,6]
lst2 = [1,2,3,4,5]

n1 = len(lst1)
n2 = len(lst2)

print(f"even % {n1 % 2}")
print(f"odd % {n2 % 2}")
print(f"even // {n1 // 2}")
print(f"odd // {n2 // 2}")
# lst3 = [0]
# lst4 = [0]
#
# print(lst3 == lst4)
#
# print(lst2 in lst1)
#
# for i in range(4, 4):
#     print(f"i:{i}")
# print(range(3, 4))
exit(0)
print(type(dp))
print(type(dp1))
print(type(dp2))

nums = [1,2,3,4,5,6,7,8,9]

print(nums[nums.index(3):nums.index(7)+1])

exit(0)

print(17/5) # floating number
print(17//5) # remainder
print(17%5) # quotient

print(format(21, '032b')[::-1])
print(int(format(21, '032b')[::-1], 2))

print(format(-21, '032b'))
print(int(format(-21, '032b')[::-1], 2))

print(format(21 & 0xFFFFFFFF, '032b'))
print(int(format(21 & 0xFFFFFFFF, '032b'), 2))

print(format(-21 & 0xFFFFFFFF, '032b'))
print(int(format(-21 & 0xFFFFFFFF, '032b'), 2))
exit(0)
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

