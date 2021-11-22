def solution(rows, columns, queries):
    answer = []
    cube = []

    for i in range(rows):
            list_tmp = []
            for j in range(columns):
                list_tmp.append(i * columns + j + 1)
            cube.append(list_tmp)



    for query in queries:
        #query = queries[0]

        for i in range(4):
            query[i] -= 1

        #print(cube)
        #첫줄부터
        x1, y1, x2, y2 = query
        list_min = []

        #print(cube)

        tmp = cube[x1][y2]  # [1][3] 정보를 보관
        list_min.append(tmp)
        for i in range(y2, y1, -1):
            cube[x1][i] = cube[x1][i-1] 
            list_min.append(cube[x1][i])

        cube[x1][y1] = cube[x1+1][y1]
        list_min.append(cube[x1][y1])

        tmp2 = cube[query[2]][query[3]]  # [4][3] 정보를 보관
        list_min.append(tmp2)

        for i in range(query[2], query[0], -1):
            cube[i][query[3]] = cube[i-1][query[3]]
            list_min.append( cube[i][query[3]])
        cube[query[0]+1][query[3]] = tmp
        list_min.append(cube[query[0]+1][query[3]])


        tmp = cube[query[2]][query[1]]  #[4][1] 정보를 보관
        list_min.append(tmp)
        for i in range(query[1], query[3], 1):
            cube[query[2]][i] = cube[query[2]][i+1]
            list_min.append( cube[query[2]][i] )
        cube[query[2]][query[3]-1] = tmp2
        list_min.append(cube[query[2]][query[3]-1])
        

        for i in range(query[0]+1, query[2], 1):
            cube[i][query[1]] = cube[i+1][query[1]]
            list_min.append( cube[i][query[1]] ) 
        cube[query[2]-1][query[1]] = tmp
        list_min.append( cube[query[2]-1][query[1]])
        
        set_min = set(list_min)
        answer.append(min(set_min))
        #print(min(list_min))
        #print(cube)

    return answer

#solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]] )
    
print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]] ))