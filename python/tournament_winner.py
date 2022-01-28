competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]

results = [0,0,1]

winner = {}

for i in range(len(competitions)):
    if results[i] == 0:
        if competitions[i][1] in winner:
            winner[competitions[i][1]] = winner[competitions[i][1]]+ 3
        else:
            winner[competitions[i][1]] = 3
    elif results[i] == 1:
        if competitions[i][0] in winner:
            winner[competitions[i][0]] = winner[competitions[i][0]]+ 3
        else:
            winner[competitions[i][0]] = 3

print('winner', winner)

