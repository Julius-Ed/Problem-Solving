"""
Median Stream Brute Force Solution
O(n^2log(n))
"""

def find_Median_brute_force(arr):

    medians = []

    for index in range(len(arr)):
        left_of_index_arr = arr[:index + 1]
        left_of_index_arr.sort()

        if len(left_of_index_arr) % 2 == 0:
            med_index = (len(left_of_index_arr) // 2) - 1
            x_med = (left_of_index_arr[med_index] +
                     left_of_index_arr[med_index + 1]) // 2
        else:
            med_index = ((len(left_of_index_arr) + 1) // 2) - 1
            x_med = left_of_index_arr[med_index]

        medians.append(x_med)

    return medians


"""
Median Stream Optimized Solution
O(n*log(n))
"""
import heapq

def find_Median(arr):
    
    medians = []

    # storing the bigger values
    min_heap = []
    # storing the smaller values
    max_heap = []


    heapq.heappush(min_heap, arr[0])
    medians.append(arr[0])

    for current in range(1, len(arr)):
        
        if arr[current] < min_heap[0]:
            heapq.heappush(max_heap, arr[current] * -1)
        else:
            heapq.heappush(min_heap, arr[current])
        
        rebalance(min_heap, max_heap)

        if (len(min_heap) + len(max_heap)) % 2 == 0:
            medians.append((min_heap[0] + (max_heap[0] * -1)) // 2)
        else:
            medians.append(min_heap[0])

      
    return medians

def rebalance(min_heap, max_heap):

    if len(min_heap) - 1 > len(max_heap):
        heapq.heappush(max_heap, heapq.heappop(min_heap) * -1)
    
    if len(max_heap) > len(min_heap):
        heapq.heappush(min_heap, heapq.heappop(max_heap) * -1)



# Test Cases
print(find_Median([5, 15, 1, 3]) == [5, 10, 5, 4])
print(find_Median([2, 4, 7, 1, 5, 3]) == [2, 3, 4, 3, 4, 3])
print(find_Median([118909791, 700266, 910518540, 704224004, 584194752]) == [
      118909791, 59805028, 118909791, 411566897, 584194752])
print(find_Median([821655781, 371962661, 134165672, 509919931, 756390024]) == [
      821655781, 596809221, 371962661, 440941296, 509919931])
print(find_Median([940574843, 812546008, 608939753, 147290660, 754850170]) == [
      940574843, 876560425, 812546008, 710742880, 754850170])
print(find_Median([641816826, 526106912, 918864393, 865296662, 169299284]) == [
      641816826, 583961869, 641816826, 753556744, 641816826])
print(find_Median([616081688, 550242654, 613849218, 93071543, 919901601]) == [
      616081688, 583162171, 613849218, 582045936, 613849218])
print(find_Median([532967393, 140365306, 216368585, 871495666, 752764578]) == [
      532967393, 336666349, 216368585, 374667989, 532967393])
print(find_Median([86361673, 842200102, 849027549, 788864989, 243392747]) == [
      86361673, 464280887, 842200102, 815532545, 788864989])
print(find_Median([792138484, 266289965, 596895321, 73846329, 747025782]) == [
      792138484, 529214224, 596895321, 431592643, 596895321])
print(find_Median([963027812, 930471055, 254401899, 868853980, 389985982]) == [
      963027812, 946749433, 930471055, 899662517, 868853980])
print(find_Median([298045834, 844177996, 889606000, 109545381, 134929387]) == [
      298045834, 571111915, 844177996, 571111915, 298045834])
