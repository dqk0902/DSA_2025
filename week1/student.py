def check_number(number):
    n = len(number)
    co_efficient = [3,7,1]
    sum = 0
    if n != 9 or number[0] != "0":
        return False
    else:
        for i in range(n-1):
            sum += int(number[i]) * co_efficient[i % 3]
        return (sum + int(number[-1])) % 10 == 0

if __name__ == "__main__":
    # Test cases
    print(check_number("012749138"))  # Expected: False
    print(check_number("012749139"))  # Expected: True
    print(check_number("013333337"))  # Expected: True
    print(check_number("012345678"))  # Expected: False
    print(check_number("012344550"))  # Expected: True
    print(check_number("1337"))       # Expected: False
    print(check_number("0127491390")) # Expected: False
    print(check_number("100000007")) # Expected: False