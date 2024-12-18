def count(a, b):
    index_a = []
    index_b = []
    b_dict = {}
    count = 0

    for i in range(len(a)):
        index_a.append(i)
    
    for i in range(len(b)):
        b_dict[b[i]] = i

    for i in a:
        index_b.append(b_dict[i])
    
    for i in index_a:
        if i < index_b[i]:
            count += 1
    
    return count

if __name__ == "__main__":
    print(count([2,3,4,1], [1,2,3,4])) # 3 
    print(count([1,2,3,4], [1,2,3,4])) # 0 
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5