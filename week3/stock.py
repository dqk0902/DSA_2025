def find_profits(prices):
    if not prices:
        return []

    profits = []
    min_price = prices[0] 

    for i in range(len(prices)):
        profit = max(0, prices[i] - min_price)
        profits.append(profit)

        if prices[i] < min_price:
            min_price = prices[i]

    return profits


if __name__ == "__main__":
    print(find_profits([1, 2, 3, 4]))  # [0, 1, 2, 3]
    print(find_profits([4, 3, 2, 1]))  # [0, 0, 0, 0]
    print(find_profits([1, 1, 1, 1]))  # [0, 0, 0, 0]
    print(find_profits([2, 4, 1, 3]))  # [0, 2, 0, 2]
    print(find_profits([1, 1, 5, 1]))  # [0, 0, 4, 0]
    print(find_profits([3, 2, 3, 5, 1, 4]))  # [0, 0, 1, 3, 0, 3]

    # Large test case
    prices = list(range(1, 10**5 + 1))
    print(find_profits(prices)[:5])  # [0, 1, 2, 3, 4]