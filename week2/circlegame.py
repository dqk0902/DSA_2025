def create(n):
    circle = []
    for i in range(1, n+1):
        circle.append(i)
    
    removed_list = []
    even_index = []
    odd_index = []

    for i in range(n):
        if i % 2 == 0:
            even_index.append(i)
        else:
            odd_index.append(i)
    
    ## first round of removing
    for index in odd_index:
        removed_list.append(circle[index])
    for index in range(1, len(odd_index)+1):
        circle.pop(index)

    ## remaining rounds of removing
    while len(circle) > 0:
        for index in even_index:
            if index < len(even_index) and index < len(circle):
                removed_list.append(circle[index])
        for index in range(len(even_index)):
            if index < len(even_index) and index < len(circle):
                circle.pop(index)    

    return removed_list

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(4)) # [2,4,1,3]
    print(create(5)) # [2,4,1,5,3]
    print(create(6)) # [2,4,6,1,5,3]
    print(create(7)) # [2,4,6,1,5,3,7]
    print(create(8)) # [2,4,6,8,1,5,3,7]
    print(create(9)) # [2,4,6,8,1,5,9,3,7]
    print(create(10)) # [2,4,6,8,10,1,5,9,3,7]