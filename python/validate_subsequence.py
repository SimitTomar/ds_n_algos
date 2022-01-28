list = [5,1,22,25,6,-1,8,10]
seq = [1,6,-1,10]


list_sorted = sorted(list)
seq_sorted = sorted(seq)

print('list_sorted', list_sorted)
print('seq_sorted', seq_sorted)

for i in range(len(seq_sorted) -1):
    if seq_sorted[i] in []