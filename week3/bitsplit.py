def count_splits(sequence):
    balance = 0
    count_map = {0: 1}
    result = 0

    for char in sequence:
        if char == '1':
            balance += 1
        else:
            balance -= 1

        if balance in count_map:
            result += count_map[balance]
            count_map[balance] += 1
        else:
            count_map[balance] = 1

    return result

if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999