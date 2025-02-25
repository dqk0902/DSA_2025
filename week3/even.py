def count_sublists(numbers):
    n = len(numbers)
    count = 0
    current_run = 0
    
    for num in numbers:
        if num % 2 == 0: 
            current_run += 1
            count += current_run
        else:
            current_run = 0
    
    return count

if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6]))  # 4
    print(count_sublists([1, 2, 3, 4]))  # 2
    print(count_sublists([1, 1, 1, 1]))  # 0
    print(count_sublists([2, 2, 2, 2]))  # 10
    print(count_sublists([1, 1, 2, 1]))  # 1

    numbers = [2] * 10**5
    print(count_sublists(numbers))  # 5000050000