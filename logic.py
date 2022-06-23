def check(list):
    for each in range(len(list)):
        temp = list(each)
        list.pop(each)
        for i in range(list):
            if i == temp:
                final = 1
                list.insert(each, temp)
                return final, each
            if  i != temp:
                final = 0
                list.insert(each, temp)
                return final, each
