from collections import Counter
def count_splits(numbers):
    left_set = set()
    right_count = Counter(numbers)
    
    valid_splits = 0
    
    for num in numbers[:-1]:  
        left_set.add(num)  
        right_count[num] -= 1 
        if right_count[num] == 0:
            del right_count[num] 
        
        if left_set == right_count.keys():
            valid_splits += 1
    
    return valid_splits

if __name__ == "__main__":
    print(count_splits([1, 1, 1, 1])) # 3
    print(count_splits([1, 1, 2, 1])) # 0
    print(count_splits([1, 2, 1, 2])) # 1
    print(count_splits([1, 2, 3, 4])) # 0
    print(count_splits([1, 2, 1, 2, 1, 2])) # 3

    numbers = [1, 2] * 10**5
    print(count_splits(numbers)) # 199997
    numbers = list(range(1, 10**5 + 1)) * 2
    print(count_splits(numbers)) # 1