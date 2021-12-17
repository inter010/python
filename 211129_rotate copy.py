from collections import deque 

def solution(s):
    answer = 0
    l_s = deque(s)

    for x in range(len(s)):
        l_s.rotate(-1)
        stack = []

        for i in range(len(l_s)):
            if l_s[i] == "(" or l_s[i] == "{" or l_s[i] == "[":
                stack.append(l_s[i])
                continue
            
            else:
                if not stack: break
                q = stack.pop()
                if q!="(" and l_s[i] ==")":
                    break
                elif q!="{" and l_s[i] =="}":
                    break
                elif q!="[" and l_s[i] =="]":
                    break

            if len(stack)==0 and i == len(l_s)-1:
                answer += 1

    return answer

print(solution("}]()[{"))