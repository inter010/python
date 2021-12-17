from collections import deque

def solution(maps):
    answer = 0
    dict_maps = {}

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            dict_maps[ i,j ] = maps[i][j]

    print(dict_maps)
    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))