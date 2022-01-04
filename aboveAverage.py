def aboveAverageSubarrays(A):

    results = []
    
    sub_array_sum = 0
    sub_array_length = 0

    rest_sum = sum(A)
    rest_length = len(A)

    for i in range(len(A)):
        for j in range(i, len(A)):

            sub_array_sum += A[j]
            sub_array_length += 1

            rest_sum -= A[j]
            rest_length -= 1


            if sub_array_sum == 0 or sub_array_length == 0:
                continue
            
            if rest_sum == 0 or rest_length == 0:
                results.append([i + 1, j + 1])
                continue

            if (sub_array_sum / sub_array_length) > (rest_sum / rest_length):

                results.append([i + 1, j + 1])
        
        sub_array_sum -= A[i]
        sub_array_length -= 1

        rest_sum += 1
        rest_length += 1

    return results

print(aboveAverageSubarrays([3, 4, 2]))