def count_pairs(numbers):
    if len(numbers) < 2:
        return 0

    sorted_numbers = sorted(numbers)
    
    pairs = 0
    small_index = 0
    large_index = 0

    while small_index < len(sorted_numbers):
        while large_index < len(sorted_numbers) and sorted_numbers[large_index] < 2 * sorted_numbers[small_index]:
            large_index += 1
        
        if large_index < len(sorted_numbers) and large_index > small_index:
            pairs += 1
            small_index += 1
            large_index += 1
        else:
            small_index += 1
        
        large_index = max(large_index, small_index + 1)

    return pairs

if __name__ == "__main__":
    print(count_pairs([1])) # 0
    print(count_pairs([1, 2, 3])) # 1
    print(count_pairs([1, 2, 3, 4])) # 2
    print(count_pairs([1, 1, 1, 1])) # 0
    print(count_pairs([10**9, 1, 1, 1])) # 1
    print(count_pairs([4, 5, 1, 4, 7, 8])) # 2
    print(count_pairs([1, 2, 3, 2, 4, 6])) # 3

    numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
    print(count_pairs(numbers)) # 41176