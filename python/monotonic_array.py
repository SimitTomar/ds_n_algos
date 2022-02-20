def check_monotonic_order(order, _monotonic_list):

    total_diff = _monotonic_list[0] - _monotonic_list[1]
    # first_two_elements_diff = 32-28 = 4
    # first_two_elements_diff = 32-20 = 12

    i = 1
    j = len(_monotonic_list)-1

    while i < j:
        current_diff = i-(i+1)
        # diff = 28 - 20 = 8
        # diff = 20 - 28 = -8
        total_diff = total_diff + current_diff
        # total_diff = 4 + 8 = 12
        # total_diff = 12 + (-8) = 4


        if total_diff >= current_diff:
            pass



                



    
    





montonic_list = [32, 28, 20, 20, 12, 5, 1] #decreasing order
montonic_list = [32, 20, 28, 20, 12, 5, 1] #decreasing order

# montonic_list = [1, 5, 12, 20, 20, 28, 32]
# montonic_list = [-1, -5, -12, -20, -20, -28, -32]
is_monotonic_list(montonic_list)