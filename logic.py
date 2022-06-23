#[5, 1, 2, 2]
def check(list):
    for each in range(len(list)):
        num = each
        temp = list[num]
        list.pop(num)
        #print(f"Rnum:{list}")
        for i in list:
            #print(f"{i} == {temp}/{num}")
            if i == temp:
                final = 1
                list.insert(num, temp)
                return final, num
            if i != temp:
                final = 0
        list.insert(num, temp)
    return final, num