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
    
    if n == 1:
      removed_list.append(circle[0])
    else: 
        for index in odd_index:
            removed_list.append(circle[index])
        for index in range(1, len(odd_index)+1):
            circle.pop(index)
        while len(circle) > 0:
            if len(circle) % 2 == 0 or len(circle) == 1:
                for index in even_index:
                    if index < len(even_index) and index < len(circle):
                        removed_list.append(circle[index])
                for index in range(len(even_index)):
                    if index < len(even_index) and index < len(circle):
                        circle.pop(index)
            else:
                for index in odd_index:
                    if index < len(odd_index) and index < len(circle):
                        removed_list.append(circle[index])
                for index in range(1, len(odd_index)):
                    if index < len(odd_index) and index < len(circle):
                        circle.pop(index)        

    return removed_list

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(4)) # [2,4,1,3]
    print(create(6)) # [2,4,6,3,1,5]
    print(create(7)) # [2,4,6,1,5,3,7]