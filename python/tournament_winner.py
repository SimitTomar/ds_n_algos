
# winner = {}

# for i in range(len(competitions)):
#     if results[i] == 0:
#         if competitions[i][1] in winner:
#             winner[competitions[i][1]] = winner[competitions[i][1]]+ 3
#         else:
#             winner[competitions[i][1]] = 3
#     elif results[i] == 1:
#         if competitions[i][0] in winner:
#             winner[competitions[i][0]] = winner[competitions[i][0]]+ 3
#         else:
#             winner[competitions[i][0]] = 3

# print('winner', winner)


def get_tournament_winner(competitions, results):

    i = 0
    j = 0
    competetions_len = len(competitions)
    results_len = len(results)
    current_best_team = ''
    scores = {current_best_team: 0}

    while i < competetions_len and j < results_len:
        if results[j] == 0:
            if competitions[i][1] in scores:
                scores[competitions[i][1]] = scores[competitions[i][1]] + 3
            else:
                scores[competitions[i][1]] = 3
            
            if scores[competitions[i][1]] > scores[current_best_team]:
                current_best_team = competitions[i][1]
        else:
            if competitions[i][0] in scores:
                scores[competitions[i][0]] = scores[competitions[i][0]] + 3
            else:
                scores[competitions[i][0]] = 3

            if scores[competitions[i][0]] > scores[current_best_team]:
                current_best_team = competitions[i][0]
        
        i+=1
        j+=1
    
    return current_best_team

competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["C#", "HTML"]
]

results = [0,0,1,1,1,0]
# [C#, Python, Python, HTML, Python, HTML]
tournament_winner = get_tournament_winner(competitions, results)
print('tournament_winner', tournament_winner)