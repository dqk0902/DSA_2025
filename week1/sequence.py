def generate(n):
    sequenceList = []
    temp = 1

    while len(sequenceList) < n:
        str_num = str(temp)
        if str_num[0] == str_num[-1]:  
            sequenceList.append(temp) 
        temp += 1 

    return sequenceList[n - 1]   

if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 2
    print(generate(3)) # 3
    print(generate(10)) # 11
    print(generate(123)) # 1141