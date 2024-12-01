import math
def count(a, b, c):
    # find minimum of a and b
    min_value_candies = a
    if b < a:
        min_value_candies = b
    
    return math.floor(c/min_value_candies)

if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4