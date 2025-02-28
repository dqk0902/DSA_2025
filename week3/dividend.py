def find_profits(prices):
    if not prices:
        return []

    profits = []
    min_price = prices[0] 
    good_day = 0

    for i in range(len(prices)):
        if prices[i] + i <= min_price + good_day: # to find the best day to buy :)
            min_price = prices[i]
            good_day = i

        profit = max(0, prices[i] - min_price + i - good_day)
        profits.append(profit)

    return profits

if __name__ == "__main__":
    
    print(find_profits([7, 10, 4, 9, 1, 9])) # [0, 4, 0, 6, 0, 9]
