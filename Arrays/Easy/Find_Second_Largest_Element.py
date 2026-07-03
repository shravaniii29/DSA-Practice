# Find Second Largest Element in an Array

n = int(input())
arr = list(map(int, input().split()))

largest = float('-inf')
second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("No second largest element")
else:
    print(second)
