coins = [5, 7, 1, 1, 2, 3, 22]


coins_sorted = sorted(coins)

print(coins_sorted)
# [1, 1, 2, 3, 5, 7, 22]
prev_num = 0

def non_constructible_change(coins_sorted, prev_num):
    for i in range(len(coins_sorted) - 1):
        sum = prev_num + coins_sorted[i]        
        if coins_sorted[i+1] > (sum + 1):
            return sum + 1
        else:
            prev_num = sum


non_constructible_num = non_constructible_change(coins_sorted, prev_num)
print('non_constructible_num', non_constructible_num)