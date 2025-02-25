def find_number(t):
    unique = set(t)
    result = t[0]
    count = 0

    for i in range(len(t)):
        if t[i] == t[0]:
            count += 1
    
    if count > 1:
        result = unique.difference({t[0]}).pop()
    
    return result

if __name__ == "__main__":
    print(find_number([1, 1, 1, 2])) # 2
    print(find_number([1, 1, 2, 1])) # 2
    print(find_number([1, 2, 1, 1])) # 2
    print(find_number([2, 1, 1, 1])) # 2
    print(find_number([1,5,5])) # 1
    print(find_number([1, 100, 1])) # 100

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers)) # 2