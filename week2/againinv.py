def create(n, k):
    result = []
    k_break = [0]
    k_pointer = 0
    for i in range(n):
        result.append(i+1)

    for i in range(n-1):
        k_pointer += n-1-i
        k_break.append(k_pointer)

    loops = 0
    for i in range(len(k_break)):
        if k == k_break[i] or k < k_break[i+1]:   
            loops += i
            break

    for loop in range(loops):
        last_ele = result.pop(n - 1)
        result.insert(loop, last_ele)
    
    if k not in k_break:
        ele = result.pop(k - k_break[loops] + loops)
        result.insert(loops, ele)
    
    return result

if __name__ == "__main__":
    print(create(3, 0)) # [1,2,3]
    print(create(3, 1)) # esim. [2,1,3]
    print(create(3, 2)) # esim. [3,1,2]
    print(create(5, 3)) # [4,1,2,3,5]
    print(create(5, 4)) # [5,1,2,3,4]
    print(create(5, 5)) # [5,2,1,3,4]
    print(create(5, 6)) # [5,3,1,2,4]
    print(create(5, 7)) # [5,4,1,2,3]
    print(create(5, 8)) # [5,4,2,1,3]
    print(create(5, 9)) # [5,4,3,1,2]
    print(create(5,10)) # [5,4,3,2,1]
    print(create(6,13)) # [6,5,4,2,1,3]