def find(t):
    result = 0

    for i in range(1,len(t)):
        if t[i] == t[i-1]:
            result = t[i]
    

    for i in range(len(t)):
        if t[i] != result:
            result = t[i]
            break
    
    return result

if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5