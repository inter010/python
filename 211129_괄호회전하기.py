def solution(s):
    answer = 0
    dict_s = {"{}":0, "[]":0, "()": 0}

    if s.count("{") + s.count("[") + s.count("(") - s.count(")") - s.count("]") - s.count("}") != 0:
        return 0

    for i in s:
        if i == "{":
            dict_s["{}"] += 1
        elif i == "}":
            dict_s["{}"] -= 1
            if dict_s["{}"] < 0: 
                dict_s= dict_s.fromkeys(["{}","[]","()"], 0 )
                s += s[0:1]
                s = s[1:]
                continue
        
        if i == "(":
            dict_s["()"] += 1
        elif i == ")":
            dict_s["()"] -= 1
            if dict_s["()"] < 0: 
                dict_s= dict_s.fromkeys(["{}","[]","()"], 0 )
                s += s[0:1]
                s = s[1:]
                continue
        
        if i == "[":
            dict_s["[]"] += 1
        elif i == "]":
            dict_s["[]"] -= 1
            if dict_s["[]"] < 0: 
                dict_s= dict_s.fromkeys(["{}","[]","()"], 0 )
                s += s[0:1]
                s = s[1:]
                continue

        answer += 1
        dict_s= dict_s.fromkeys(["{}","[]","()"], 0 )
        s += s[0:1]
        s = s[1:]

    return answer

print(solution("[)(]"))