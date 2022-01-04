def aboveAverageSubarrays(A):

    results = []

    sub_array_sum = 0
    sub_array_length = 0

    rest_sum = sum(A)
    rest_length = len(A)

    # loop through all possible sub_arrays O(n^2).
    for i in range(len(A)):
        for j in range(i, len(A)):

            # add new number to sub-array and incrase length.
            sub_array_sum += A[j]
            sub_array_length += 1

            # subtract new number from the remaining elements and decrease count.
            rest_sum -= A[j]
            rest_length -= 1

            # if sum of sub-array is zero it's average can't be larger then the average of the remaining elemnts.
            if sub_array_sum == 0 or sub_array_length == 0:
                continue

            # if sum of remaining elemnts equals 0 sub-string's average must be greater.
            if rest_sum == 0 or rest_length == 0:
                results.append([i + 1, j + 1])
                continue

            if (sub_array_sum / sub_array_length) > (rest_sum / rest_length):
                results.append([i + 1, j + 1])

        # in this iteration the sub-array gets narrower, elements must be subtracted and added accordingly.
        sub_array_sum = 0
        sub_array_length = 0

        rest_sum = sum(A)
        rest_length = len(A)

    return results


print(aboveAverageSubarrays([3,4,2])==[[1, 2], [1, 3], [2, 2]])
print(aboveAverageSubarrays([2]) == [[1,1]])
print(aboveAverageSubarrays([2,2,2,2])==[[1,4]])
print(aboveAverageSubarrays([2,2,2,1])==[[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [3, 3]])
print(aboveAverageSubarrays([3,4,2,5,6]) == [[1, 5], [2, 5], [3, 5], [4, 4], [4, 5], [5, 5]])
print(aboveAverageSubarrays([1,4,2,10,20,30,50,60,5,1000000])==[[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 10]])
