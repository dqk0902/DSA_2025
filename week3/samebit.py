def count(s):
    zeros = 0
    ones = 0
    for i in range(len(s)):
        if s[i] == "0":
            zeros += 1
        if s[i] == "1":
            ones += 1
    
    zero_ways = zeros * (zeros - 1) // 2 
    ones_ways = ones * (ones - 1) // 2   

    return zero_ways + ones_ways

if __name__ == "__main__":
    print(count("0101")) # 2
    print(count("000000")) # 15
    print(count("000111")) # 6
    print(count("00100001101100")) # 46