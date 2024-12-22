def count(t):
    result = 0

    for i in range(len(t)):
        for j in range(len(t)):
            if i < j and t[i] > t[j]:
                result += 1

    return result

# O(n2) time complexity

if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([5,4,3,1,2])) # 9
    print(count([1,2,3,4,5,6,7])) # 0
    print(count([1,8,2,7,3,6,4,5])) # 12
