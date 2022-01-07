"""
 Best Time to Buy and Sell Stock I
"""


def max_profit(arr):

    lowest = 0
    highest = 0
    current = 0

    seen_min = 0

    for current in range(len(arr)):

        if arr[current] < arr[seen_min]:
            seen_min = current

        if arr[current] - arr[seen_min] > arr[highest] - arr[lowest]:
            highest = current
            lowest = seen_min

    return arr[highest] - arr[lowest]


print(max_profit([7, 1, 5, 3, 6, 4]))
