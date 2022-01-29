def move_element_to_end(element_list, num):

    sorted_elemet_list = sorted(element_list)
    # [1, 2, 2, 2, 2, 2, 3, 4]
    sorted_elemet_list_len = len(sorted_elemet_list)
    i = 0
    while i < range(sorted_elemet_list_len):

        current_idx = i
        if sorted_elemet_list[i] < num:
            i+=1
        elif sorted_elemet_list[i] == num:
            del sorted_elemet_list[i]
            sorted_elemet_list.append(num)
            i = current_idx
        elif sorted_elemet_list[i] > num:
            break
            
    
    return sorted_elemet_list


element_list = [2, 1, 2, 2, 2, 3, 4, 2]
num = 2

move_element_list = move_element_to_end(element_list, num)
print('move_element_list', move_element_list)