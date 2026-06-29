arr = [10, 5, 8, 20, 15]

target = 20

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index", i)
        break
else:
    print("Element not found")