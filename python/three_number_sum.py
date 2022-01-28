num_list = [12, 3, 1, 2, -6, 5, -8, 6]
target_sum = 0


sorted_list = sorted(num_list)
# [-8, -6, 1, 2, 3, 5, 6, 12]
print('sorted_list', sorted_list)

def get_three_num_sum(sorted_list, target_sum):
    current_num_index = 0
    i = current_num_index+1
    j = len(sorted_list)-1
    sum_list = []
    while current_num_index < len(sorted_list)-2:
        current_num = sorted_list[current_num_index]
        left_pointer = sorted_list[i]
        right_pointer = sorted_list[j]
        print('current_num', current_num)
        print('left_pointer', left_pointer)
        print('right_pointer', right_pointer)
        if i==j-1:
            if (current_num + left_pointer + right_pointer) == target_sum:
                sum_list.append([current_num, left_pointer, right_pointer])
            current_num_index+=1
            i = current_num_index + 1
            j = len(sorted_list)-1
        elif (current_num + left_pointer + right_pointer) == target_sum:
            sum_list.append([current_num, left_pointer, right_pointer])
            i+=1
            j-=1
        elif (current_num + left_pointer + right_pointer) > target_sum:
            j-=1
        elif (current_num + left_pointer + right_pointer) < target_sum:
            i+=1


    print('sum_list', sum_list)
    return sum_list

three_num_sum = get_three_num_sum(sorted_list, target_sum)
print('three_num_sum', three_num_sum)

