def solution(ip):
    answer = 0
    list_s = list(ip)
    stack = []

    if ip.count("{") + ip.count("[") + ip.count("(") - ip.count(")") - ip.count("]") - ip.count("}") != 0:
        return 0

    for i in range(len(ip)):
        list_s.append(list_s[0])
        list_s = list_s[1:]

        for j in range(len(list_s)):
            if list_s[j] == "(" or list_s[j] == "[" or list_s[j] == "{":
                stack.append(list_s[j])
                continue
            else:
                if not stack : break
                else: last = stack.pop()
                if last == "(" and list_s[j] != ")":
                    break
                elif last == "[" and list_s[j] != "]":
                    break
                elif last == "{" and list_s[j] != "}":
                    break

            if j == len(list_s)-1:
                answer += 1

    return answer

print(solution(")[(]"))