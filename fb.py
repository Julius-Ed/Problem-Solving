
"""
1st exercise.
"""


def ocean_view(arr_heights):

    if len(arr_heights) == 0:
        return None

    # loop backwards through string, starting at the second last element.
    for i in range(len(arr_heights) - 2, -1, -1):
        # if an element has a greater neighbour on the right hand side, it can't see the ocean.
        # all of the houses on the RHS of this elementcan see the ocean then.
        if arr_heights[i] < arr_heights[i + 1]:
            break

    result = [x for x in range(i + 1, len(arr_heights))]

    return result


# print(ocean_view([3, 1, 2, 4, 3, 2]) == [3, 4, 5])
# print(ocean_view([1, 2, 3, 4, 5]) == [4])
# print(ocean_view([]) == None)


"""
2nd exercise.
"""
import copy

def trucker(weights, time):

    # find upper boundary for the capacity.
    max_capacity = sum(weights)

    # count down from the max capacity until the trucking can't be made in the alotted time.
    for capacity in range(max_capacity, -1, -1):
        if truckable_in_time(weights, capacity, time) == False:
            return capacity + 1

    return capacity


def truckable_in_time(weights, capacity, time):
    # checks given weight, capacity, and alloted time whether a shipment can be made.
    copy_weights = copy.copy(weights)

    load = 0
    days = 0

    while days < time:
        while load <= capacity:
            if len(copy_weights) == 0:
                return True
            load += copy_weights.pop()

        days += 1
        load = 0

    return False


print(trucker([5, 2, 1, 8], 2) == 8)
