def count(s):
    n = len(s)
    ## sliding window
    left = 0
    count = 0
    char_count = {'t': 0, 'i': 0, 'r': 0, 'a': 0}

    for right in range(n):
        if s[right] in char_count:
            char_count[s[right]] += 1
        while char_count['t'] > 0 and char_count['i'] > 0 and char_count['r'] > 0 and char_count['a'] > 0:
            count += n - right
            if s[left] in char_count:
                char_count[s[left]] -= 1
            left += 1
    return count
    

if __name__ == "__main__":
    print(count("aybabtu")) # 0
    print(count("tira")) # 1
    print(count("ritari")) # 6
    print(count("tiratiratira")) # 45
    print(count("xaxrxixtx")) # 4