def count_sublists(numbers):
    if not numbers:
        return 0
    
    n = len(numbers)
    count = n
    
    current_run = 1
    
    for i in range(1, n):
        if numbers[i] > numbers[i-1]:  
            current_run += 1
            count += current_run - 1 
        else:
            current_run = 1 
    
    return count

if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4]))  # 7
    print(count_sublists([1, 2, 3, 4]))  # 10
    print(count_sublists([4, 3, 2, 1]))  # 4
    print(count_sublists([1, 1, 1, 1]))  # 4
    print(count_sublists([1, 2, 1, 2]))  # 6

    numbers = list(range(1, 10**5+1))
    print(count_sublists(numbers))  # 5000050000