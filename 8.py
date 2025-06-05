# Задание 1
n = int(input())
numbers = [int(input()) for _ in range(n)]
print(' '.join(map(str, reversed(numbers))))

# Задание 2
number = int(input())
arr = list(map(int, input().split()))
if number > 1:
    arr = [arr[-1]] + arr[:-1]
print(' '.join(map(str, arr)))

# Задание 3
ms = int(input())
ns = int(input())
weights = [int(input()) for _ in range(ns)]
weights.sort()

left = 0
right = n - 1
boats = 0

while left <= right:
    if weights[left] + weights[right] <= ms:
        left += 1
    right -= 1
    boats += 1

print(boats)