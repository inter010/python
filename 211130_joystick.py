def distance(s):
    if s == "A":  return 0
    l_comp = []

    l_comp.append(ord(s) - ord("A"))
    l_comp.append(ord("Z")-ord(s) + 1)

    return min(l_comp)


def solution(name):
    answer = 0
    l_distance = []
    l_index = []
    l_comp = []

    for i in range(len(name)):
        l_distance.append(distance(name[i]))
        answer += distance(name[i])
        if distance(name[i]) != 0 and i != 0:
            l_index.append(i)
    if len(name)==1:
        return distance(name)
    if not l_index : 
        return 0
    
    print(l_index)
    print(l_distance)

    # index = 0
    # while l_index:
    #     for i in l_index:
    #         l_comp.append(i-index)
    
    return answer 


print(solution("ABAAAAABB"))