def count_splits(sequence):
    n = len(sequence)
    if n % 2 != 0:
        return 0
    
    balance = [0] * (n + 1)
    for i in range(n):
        if sequence[i] == '0':
            value = -1
        else:
            value = 1
        balance[i + 1] = balance[i] + value
    
    if balance[n] != 0:
        return 0

    result = 0

    for i in range(1,n):
        if balance[i] == 0:
            result += 1

    return result


if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3
    print(count_splits("1011111010")) # 0

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999