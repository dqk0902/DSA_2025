def count_rounds(numbers):
    if not numbers:
        return 0

    rounds = 0
    next_expected = 1
    max_num = max(numbers)

    while next_expected <= max_num:
        found = False
        for num in numbers:
            if num == next_expected:
                found = True
                next_expected += 1
        if found:
            rounds += 1

    return rounds

if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 5, 4, 1, 3])) # 4
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000