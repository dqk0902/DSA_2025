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

    ## first round in the circle
    if n % 2 == 0 or n == 1:
        for index in even_index:
            removed_list.append(circle[index])
        for index in even_index:
            circle.pop(index)
    else:
        for index in odd_index:
            removed_list.append(circle[index])
        for index in odd_index:
            circle.pop(index)

    
    print('circle', circle)
    return removed_list

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,5,3,7]