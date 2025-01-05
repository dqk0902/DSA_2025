def count(t):
    n = len(t)
    smallest = t[0]
    index_smallest = []

    for i in range(n):
        if t[i] < smallest:
            smallest = t[i]
    
    for i in range(n):
        if t[i] == smallest:
            index_smallest.append(i)

    if len(index_smallest) <= 1:
        return 0
    else:
        return index_smallest[-1] - index_smallest[0]


if __name__ == "__main__":
    print(count([2,1,1,3])) # 1
    print(count([1,1,1,1])) # 3
    print(count([1,2,3,1,2,3])) # 3
    print(count([1,2,3,4,3,2,1])) # 6
    print(count([4,3,2,1,2,3,4])) # 0