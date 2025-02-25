def count_rounds(numbers):
    if len(numbers) <= 1:
        return len(numbers)

    rounds = 1
    index_map = {num: idx for idx, num in enumerate(numbers)}

    for num in numbers:
        if num + 1 in index_map and index_map[num] > index_map[num + 1]:
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