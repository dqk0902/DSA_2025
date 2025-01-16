def find(t):
    n = len(t)
    best = 0
    min_price = t[0]
    for i in range(1, n):
        min_price = min(min_price, t[i])
        best = max(best, t[i] - min_price)
    
    return best
    
if __name__ == "__main__":
    print(find([1,5,2,1,5])) # 8
    print(find([1,5,1,5])) # 4
    print(find([1,2,3,4,5])) # 4
    print(find([5,4,3,2,1])) # 0
    print(find([4,2,5,8,7,6,1,2,5,1])) # 10