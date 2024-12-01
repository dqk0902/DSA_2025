def find(s):
    n = len(s)
    
    for i in range(n):
        if n % (i + 1) == 0:
            substring = s[:i+1]
            if substring * (n // (i + 1)) == s:
                return i + 1  
    
    return n


if __name__ == "__main__":
    print(find("aaa"))           # 1
    print(find("abcd"))          # 4
    print(find("abcabcabcabc"))  # 3
    print(find("aybabtuaybabtu"))# 7
    print(find("abcabca"))       # 7