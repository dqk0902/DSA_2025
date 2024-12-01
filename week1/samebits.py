def count(s):
    result = 0
    n = len(s)
    zeros = 0
    ones = 0
    for i in range(n):
        if s[i] == "0":
            zeros += 1
        if s[i] == "1":
            ones += 1
    result = n - max(zeros, ones)
    return result

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4