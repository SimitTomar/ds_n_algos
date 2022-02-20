from cgitb import reset, small
import math
import re
import sys


# def find_smallest_difference(list_one, list_two):

#     smallest_diff_list = [None]*2
    
#     sorted_list_one = sorted(list_one)
#     # [-1, 3, 5, 10, 20, 28]
#     sorted_list_two = sorted(list_two)
#     # [15, 17, 26, 134, 135]

#     smallest_difference = 0

#     for i in range(len(sorted_list_one)):
#         for j in range(len(sorted_list_two)):
#             smallest_difference = abs(sorted_list_one[i] - sorted_list_two[j])

#             if sorted_list_one[i] == sorted_list_two[j]:
#                 smallest_diff_list[0] = sorted_list_one[i]
#                 smallest_diff_list[1] = sorted_list_two[j]

#             elif sorted_list_one[i] < sorted_list_two[j]:
#                 smallest_difference = abs(sorted_list_one[i] - sorted_list_two[j])
#                 smallest_diff_list[0] = sorted_list_one[i]
#                 smallest_diff_list[1] = sorted_list_two[j]
#                 break
#             elif sorted_list_one[i] > sorted_list_two[j]:

#                 if smallest_difference < abs(sorted_list_one[i] - sorted_list_two[j]):
#                     break
#                 else:
#                     smallest_diff_list[0] = sorted_list_one[i]
#                     smallest_diff_list[1] = sorted_list_two[j]
            
#     return smallest_diff_list



def find_smallest_difference(list_one, list_two):

    i = 0
    j = 0
    result = sys.maxsize
    smallest_diff_list = [None]*2
    # arr1 = [2, 4, 6, 8, 10]
    # arr2 = [12, 14, 16, 18, 20]

    while (i < len(list_one) and j < len(list_two)):

        if abs(list_one[i] - list_two[j]) < result:
            result = abs(list_one[i] - list_two[j])
            smallest_diff_list[0] = list_one[i]
            smallest_diff_list[1] = list_two[j]
        
        if list_one[i] < list_two[j]:
            i+=1
        else:
            j+=1

    return smallest_diff_list

list_one = [-1, 5, 10, 20, 28, 3]
list_two = [26, 134, 135, 15, 17]

smallest_difference = find_smallest_difference(list_one, list_two)
print('smallest_difference', smallest_difference)