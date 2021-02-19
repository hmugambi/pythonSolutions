def bubbleSortSol(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


#arr = [64, 34, 25, 12, 22, 11, 90]
arr = [64, 34, 25, 12, 7, 9, 11, 89, 23, 54]
bubbleSortSol(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])