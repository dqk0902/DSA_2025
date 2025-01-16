def check_year(year):
    str_year = str(year)
    list_year = []
    for i in range(len(str_year) - 1):
        if i % 2 == 0:
            list_year.append(int(str_year[i] + str_year[i + 1]))

    return sum(list_year) ** 2 == year

if __name__ == "__main__":
    # Test cases
    print(check_year(1995))  # Expected: False
    print(check_year(2024))  # Expected: False
    print(check_year(2025))  # Expected: True
    print(check_year(2026))  # Expected: False
    print(check_year(3025))  # Expected: True
    print(check_year(5555))  # Expected: False