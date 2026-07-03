# Here we have taken the first array element as our largest element initially,
# but if it is mentioned that the array contains negative elements as well, then take largest element (maxi here) as -infinity

def find_max(arr):
    maxi = arr[0]

    for num in arr:
        if num > maxi:
            maxi = num

    return maxi
