from cgitb import small
import math


def find_smallest_difference(list_one, list_two):

    smallest_diff_list = [None]*2
    
    sorted_list_one = sorted(list_one)
    # [-1, 3, 5, 10, 20, 28]
    sorted_list_two = sorted(list_two)
    # [15, 17, 26, 134, 135]

    smallest_difference = 0

    for i in range(len(sorted_list_one)):
        for j in range(len(sorted_list_two)):
            smallest_difference = abs(sorted_list_one[i] - sorted_list_two[j])

            if sorted_list_one[i] == sorted_list_two[j]:
                smallest_diff_list[0] = sorted_list_one[i]
                smallest_diff_list[1] = sorted_list_two[j]

            elif sorted_list_one[i] < sorted_list_two[j]:
                smallest_difference = abs(sorted_list_one[i] - sorted_list_two[j])
                smallest_diff_list[0] = sorted_list_one[i]
                smallest_diff_list[1] = sorted_list_two[j]
                break
            elif sorted_list_one[i] > sorted_list_two[j]:

                if smallest_difference < abs(sorted_list_one[i] - sorted_list_two[j]):
                    break
                else:
                    smallest_diff_list[0] = sorted_list_one[i]
                    smallest_diff_list[1] = sorted_list_two[j]
            
    return smallest_diff_list


list_one = [-1, 5, 10, 20, 28, 3]
list_two = [26, 134, 135, 15, 17]

smallest_diff = find_smallest_difference(list_one, list_two)
# print('smallest_diff', smallest_diff)