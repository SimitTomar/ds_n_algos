from sqlite3 import SQLITE_UPDATE


sorted_list = [1,2,3,4,6,7,9]

num_square = list(map(lambda n: n*n, sorted_list))

sorted(num_square)