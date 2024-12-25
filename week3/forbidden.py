def count(s):
    n = len(s)
    total_count = (n * (n+1)) // 2
    index_a = []
    
    for i in range (n):
        if s[i] == "a":
            index_a.append(i)

    if len(index_a) > 0:
        total_a = (index_a[0] + 1) * (n-index_a[0])
        for i in range(1, len(index_a)):
            total_a += (index_a[i] - index_a[i-1]) * (n-index_a[i])
        
        return total_count - total_a
    else:
        return total_count
    
    # worst case len(index_a) == n => k <= n => O(n) time complexity

if __name__ == "__main__":
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1
    print(count("aybabtu")) # 9