
def insertion_sort(arr):

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                else:
                    break

    return arr


print(insertion_sort([5, 1, 120, 2, -123]))
