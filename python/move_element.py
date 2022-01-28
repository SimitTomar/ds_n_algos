# from tracemalloc import start, stop


def move_element(element_list, num):

    sorted_elemet_list = sorted(element_list)
    # [1, 2, 2, 2, 2, 2, 3, 4]
    upto_index = len(sorted_elemet_list)
    i = 0
    while i < range(upto_index):

        current_idx = i
        print('current_idx', current_idx)
        if sorted_elemet_list[i] == num:
            del sorted_elemet_list[i]
            sorted_elemet_list.append(num)
            i = current_idx
            print('i', i)

        elif sorted_elemet_list[i] > num:
            break
            # del sorted_elemet_list[i]
            # print('sorted_elemet_list after del', sorted_elemet_list)
            
    
    print('sorted_elemet_list', sorted_elemet_list)
    return sorted_elemet_list



   


element_list = [2, 1, 2, 2, 2, 3, 4, 2]
num = 2

smallest_diff = move_element(element_list, num)