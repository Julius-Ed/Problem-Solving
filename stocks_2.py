"""
 Best Time to Buy and Sell Stock II
"""

def max_profit_ii(arr):

    lowest = 0
    highest = 0
    current = 0

    seen_min = 0

    profit = 0

    for current in range(len(arr)):

        if arr[current] < arr[seen_min]:
            seen_min = current

        if arr[current] - arr[seen_min] > arr[highest] - arr[lowest]:

            highest = current
            lowest = seen_min

            profit += arr[highest] - arr[lowest]

            highest = seen_min
            seen_min = current

    return profit


print(max_profit_ii([7, 1, 5, 3, 6, 4]) == 7)
print(max_profit_ii([1,2,3,4,5]) == 4)