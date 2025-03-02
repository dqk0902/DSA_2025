def count_pairs(numbers):
    sorted_numbers = sorted(numbers)
    small, large = 0, 0 
    count = 0
    n = len(sorted_numbers)
    result = []
    
    while small < n and large < n:
        if 2 * sorted_numbers[small] <= sorted_numbers[large]:
            result.append((sorted_numbers[small], sorted_numbers[large]))
            count += 1
            small += 1 
            large += 1
        else:
            large += 1

    return set(result), count

if __name__ == "__main__":
    print(count_pairs([1])) # 0
    print(count_pairs([1, 2, 3])) # 1
    print(count_pairs([1, 2, 3, 4])) # 2
    print(count_pairs([1, 1, 1, 1])) # 0
    print(count_pairs([10**9, 1, 1, 1])) # 1
    print(count_pairs([4, 5, 1, 4, 7, 8])) # 2
    print(count_pairs([1, 2, 3, 2, 4, 6])) # 3
    print(count_pairs([4, 8, 52])) # 1
    print(count_pairs([82, 10, 30, 1])) # 2
    print(count_pairs([20, 3, 1, 7, 23, 2, 10, 11, 2])) # 4

    numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
    ##print(count_pairs(numbers)) # 41176