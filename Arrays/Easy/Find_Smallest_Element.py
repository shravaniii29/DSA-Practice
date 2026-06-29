arr = [10, 5, 8, 20, 15]

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num

print("Smallest:", smallest)