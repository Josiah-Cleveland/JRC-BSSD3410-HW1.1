# Josiah Cleveland
# Homework 1.1
# BSSD 3410 (Applied Algorithms)
# 14 Aug 2024

# Python3 code to linearly search x in arr[].
def search(arr, N, x):

    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1

#==========================================

# Python3 code to implement iterative Binary
# Search.
# It returns location of x in given array arr
def binarySearch(arr, low, high, x):

    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1

#==========================================

# Driver Code
if __name__ == "__main__":

    import random
    arr = []
    for i in range(200):
        num = random.randint(1,100)
        arr.append(num)
#   print(arr)
    x = 10
    N = len(arr)


    import timeit
    iter = 10
    ltime = timeit.timeit(lambda:search(arr, N, x),\
                          setup="from __main__ import binarySearch", number=iter)
    btime = timeit.timeit(lambda:binarySearch(arr, 0, len(arr)-1, x),\
                          setup="from __main__ import binarySearch", number=iter)

    print("Linear search took:", ltime)
    print("Binary search took:", btime)



    # Function call
    result = search(arr, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)


    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

#   print(len(arr))