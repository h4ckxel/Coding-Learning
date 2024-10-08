def quicksort(arreglo):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) - 1]

    i = 0
    for j in range(len(arr)-1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[len(arr)-1] = arr[len(arr)-1], arr[i]

    quicksort(arr[0:i])
    quicksort(arr[i+1:len(arr)])

    return arr

def partition(arr, pivot):

    i = 0
    for j in range(len(arr)):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            arr[i], arr[len(arr)-1] = arr[len(arr)-1], arr[i]
            return i

arr = [4, 2, 7, 3, 1, 6]

print(quicksort(arr))

# Output: [1, 2, 3, 4, 6, 7]
