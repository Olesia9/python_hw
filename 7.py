import re
# Задание 1
s = input().strip()
if s == s[::-1]:
    print("yes")
else:
    print("no")

# Задание 2
q = input().strip()
result = re.sub(r'\s+', ' ', q)
print(result)
