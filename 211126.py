def solution(enroll, referral, seller, amount):
    answer = []
    list_prmd = []
    dict_prmd = {}
    amount = [i*100 for i in amount]
    dict_price = {}

    for i in range(len(enroll)):
        if referral[i] == "-":
            list_prmd.append([enroll[i], "me"])

            ##
            dict_prmd[enroll[i]] = "me"
        else:
            for j in list_prmd:
                if referral[i] == j[0]:
                    list_tmp = [enroll[i]]
                    list_tmp.extend(j)
                    list_prmd.append(list_tmp)
                    break

            ##    
            #dict_prmd[enroll[i]] = ','.join((referral[i], dict_prmd.get(referral[i])))
            dict_prmd[enroll[i]] = referral[i], dict_prmd[referral[i]]

    print(dict_prmd)

    for i in range(len(seller)): 
        for j in list_prmd:
            if j[0] == seller[i]:
                int_len = len(j)
                int_price = amount[i]
                
                while int_len > 0:
                    int_idx = len(j) - int_len
                    int_yourprice = int_price - int_price//10
                    int_price = int_price//10
                    if j[int_idx] in dict_price:
                        dict_price[j[int_idx]] += int_yourprice
                    else:
                        dict_price[j[int_idx]] = int_yourprice
                    int_len -= 1
                break
    
    for i in enroll:
        if i in dict_price:
            answer.append(dict_price[i])
        else:
            answer.append(0)

    #print(list_prmd)
    #print(dict_price)


    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
            ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], 
            ["sam", "emily", "jaimie", "edward"],[2, 3, 5, 4] ))