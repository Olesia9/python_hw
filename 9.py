# Задание 1
n = int(input())
numbers = list(map(int, input().split()))
unique_count = len(set(numbers))
print(unique_count)

# Задание 2
number = int(input())
list1 = [int(input()) for _ in range(number)]
m = int(input())
list2 = [int(input()) for _ in range(m)]

set1 = set(list1)
set2 = set(list2)
common = len(set1 & set2)
print(common)

# Задание 3
numbers = list(map(int, input().split()))
seen = set()

for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)
